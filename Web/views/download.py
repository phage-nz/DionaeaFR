import os, tempfile, zipfile

from wsgiref.util import FileWrapper
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import RequestContext

from django_tables2 import RequestConfig
from Web.models.download import Download
from Web.tables.download import DownloadTable
from Web.filters.download import DownloadFilter
from Web.forms.download import DownloadFilterForm


length = len(Download.objects.all())


def downloadIndex(request):
    downloads = Download.objects.all()
    filterQueryset = DownloadFilter(
        request.GET,
        queryset=downloads
    )
    table = DownloadTable(
        filterQueryset.qs
    )
    filters = DownloadFilterForm()
    RequestConfig(
        request,
        paginate={
            "per_page": 12
        }
    ).configure(
        table
    )
    return render(request, 'base.html',
        {
            'table': table,
            'filters': filters,
            'title': u'Downloads'
        }
    )

def downloadSample(request, file_md5):
    filename = os.path.join('/opt/dionaea/var/dionaea/binaries', file_md5)

    if not os.path.exists(filename):
        raise Http404

    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)                       
    archive.write(filename, '{0}.vir'.format(file_md5))
    archive.close()
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename={0}.zip'.format(file_md5)
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response

# vim: set expandtab:ts=4
