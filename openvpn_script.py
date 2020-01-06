# Скрипт для добавления в базу информации о подключенных оноплатниках

import os
from django import setup
from django.conf import settings
from django.utils.timezone import make_aware


def execute_command():    
    from sbc_monitor.models import SingleBoardComputer, Status
    from openvpn_status import parse_status

    with open(settings.PATH_TO_LOG) as logfile:
        status = parse_status(logfile.read())    
    
    mas_client = [] 
    for client_virtual_ip in status.routing_table:
        pr = status.routing_table[client_virtual_ip] # properties routing
        pc = status.client_list[str(pr.real_address)]  # properties client
        obj, _ = SingleBoardComputer.objects.get_or_create(name=pc.common_name)
        mas_client.append(Status(
            sbc=obj,
            connected_since=make_aware(pc.connected_since),
            last_ref=make_aware(pr.last_ref),
            real_address=pc.real_address,
            virtual_address=client_virtual_ip,
            updated=make_aware(status.updated_at)
        ))
    Status.objects.bulk_create(mas_client)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sbc_project.settings")
    # django.setup()
    setup()
    execute_command()
