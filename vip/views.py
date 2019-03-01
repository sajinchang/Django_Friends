from libs.http import render_json
from vip.models import Vip


def show_vip(request):
    """显示各个vip所对应的权限"""
    vip_infos = []
    for vip in Vip.objects.all():
        vip_info = vip.to_dict()
        vip_info['perm'] = []
        for perm in vip.perms():
            vip_info['perm'].append(perm)
        vip_infos.append(vip_info)

    return render_json(data=vip_infos)
