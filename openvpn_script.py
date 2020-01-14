# Скрипт для добавления в базу информации о подключенных оноплатниках


def main():
	from sbc_monitor.models import SingleBoardComputer, Status
	from django.utils import timezone
	obj_sbc, _ = SingleBoardComputer.objects.get_or_create(
	    name=os.getenv("common_name"))
	connect_time = timezone.now()
    if os.getenv("script_type") == "client-connect":
        obj_status = Status(
			sbc=obj_sbc,
			connected_since=connect_time,
			last_ref=connect_time,
			updated=connect_time,
			real_address=os.getenv("trusted_ip") + ":" + os.getenv("trusted_port"),
			virtual_address=os.getenv("ifconfig_pool_remote_ip"),
		)
		obj_status.save()
    elif os.getenv("script_type") == "client-disconnect":
        obj_status = Status(
		    sbc=obj_sbc,
		    connected_since=connect_time,
		    last_ref=connect_time,
		    updated=connect_time,
		    real_address=None,
		    virtual_address=None
	    )
	    obj_status.save()

if __name__ == "__main__":
	import os
	from django import setup
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sbc_project.settings")
	setup()
	main()


