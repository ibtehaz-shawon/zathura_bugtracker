from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from projects.models import Projects
from team.models import Team
from token_manager.models import ProjectToken
from utility.helper import (get_common_view_payload,
                            get_error_count_of_a_project, get_project_object,
                            get_project_token_by_project_id, get_user_object,
                            get_verbose_count_of_a_project, set_cookie)
from utility.token_manager import decode_token, protected


class ProjectView(View):

    @protected
    def get(self, request, project_id: str):
        payload = decode_token(request.COOKIES['access_token'])
        user = get_user_object(username=payload["sub"])
        project = get_project_object(project_id)
        if project is None:
            context = get_common_view_payload(user, "Error!")
            context["error_message"] = "This project does not exist!"
            response = render(request, 'frontend/project.html', context)
            return response

        project.created_on = datetime.timestamp(project.created_on) * 1000
        project.modified_on = datetime.timestamp(project.modified_on) * 1000

        project_token = get_project_token_by_project_id(project.pk)
        if project_token:
            project_token.generated_on = datetime.timestamp(
                project_token.generated_on) * 1000
            project_token.updated_on = datetime.timestamp(
                project_token.updated_on) * 1000

        context = get_common_view_payload(user, project.project_name)
        context["project_object"] = project
        context["project_token"] = project_token
        context["error_count"] = get_error_count_of_a_project(
            project.project_id)
        context["verbose_count"] = get_verbose_count_of_a_project(
            project.project_id)

        if "message" in request.GET:
            context["message"] = request.GET["message"]

        if "status" in request.GET:
            context["status"] = request.GET["status"]

        response = render(request, 'frontend/project.html', context)
        return response
