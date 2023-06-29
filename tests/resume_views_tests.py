from django.http import FileResponse
import os


def download_resume(request):
    resume_path = './media/Resume.pdf'
    if os.path.exists(resume_path):
        with open(resume_path, 'rb') as file:
            response = FileResponse(file)
            response['Content-Disposition'] = 'attachment; filename="RayThurmanResume.pdf"'
            return response
    else:
        return HttpResponse('Resume not found.')
