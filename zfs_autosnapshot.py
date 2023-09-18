#!/usr/bin/python

import subprocess
import datetime
import argparse

# Parsowanie argumentów linii poleceń
parser = argparse.ArgumentParser(description="Automatyczne tworzenie i zarządzanie snapshotami ZFS")
parser.add_argument("zfs_dataset", help="Ścieżka do systemu plików ZFS, który chcesz monitorować")
parser.add_argument("--hourly", type=int, help="Maksymalny wiek (w godzinach) dla snapshotów godzinnych")
parser.add_argument("--daily", type=int, help="Maksymalny wiek (w dniach) dla snapshotów dziennych")
parser.add_argument("--weekly", type=int, help="Maksymalny wiek (w tygodniach) dla snapshotów tygodniowych")
parser.add_argument("--monthly", type=int, help="Maksymalny wiek (w miesiącach) dla snapshotów miesięcznych")
args = parser.parse_args()

# Format daty i godziny, który zostanie użyty w nazwie snapshota
timestamp_format = "%Y%m%d%H%M%S"
current_time = datetime.datetime.now()

# Tworzenie nazwy snapshota z datą i godziną
if args.hourly:
    snap = "@hourly"
elif args.daily:
    snap= "@daily"
elif args.weekly:
    snaps= "@weekly"
elif args.monthly:
    snap = "@monthly"

snapshot_name = f"{args.zfs_dataset}{snap}_{current_time.strftime(timestamp_format)}"

# Komenda do tworzenia snapshota
create_snapshot_command = f"/usr/sbin/zfs snapshot {snapshot_name}"

try:
    # Wykonaj komendę do tworzenia snapshota
    subprocess.run(create_snapshot_command, shell=True, check=True)
    print(f"Utworzono snapshot: {snapshot_name}")

    # Pobierz listę wszystkich snapshotów dla danej ścieżki ZFS
    list_snapshots_command = f"/usr/sbin/zfs list -t snapshot -H -o name,creation -S creation -r {args.zfs_dataset}"
    snapshot_list = subprocess.check_output(list_snapshots_command, shell=True, text=True).strip().split('\n')

    # Usuń snapshoty, które przekroczyły maksymalny wiek
    current_time = datetime.datetime.now()
    for snapshot_info in snapshot_list:
        snapshot, creation_time_string = snapshot_info.split('\t')
        creation_datetime = datetime.datetime.strptime(creation_time_string, '%a %b %d %H:%M %Y')
        creation_timestamp = creation_datetime.timestamp()

        if snapshot.startswith(f"{args.zfs_dataset}@{snap}_"):
            max_snapshot_age_seconds = None

            if args.hourly:
                max_snapshot_age_seconds = args.hourly * 3600
            elif args.daily:
                max_snapshot_age_seconds = args.daily * 86400
            elif args.weekly:
                max_snapshot_age_seconds = args.weekly * 604800
            elif args.monthly:
                max_snapshot_age_seconds = args.monthly * 2629746

            if max_snapshot_age_seconds is not None and (current_time.timestamp() - creation_timestamp) > max_snapshot_age_seconds:
                delete_snapshot_command = f"/usr/sbin/zfs destroy {snapshot}"
                subprocess.run(delete_snapshot_command, shell=True)
                print(f"Usunięto stary snapshot: {snapshot}")

except subprocess.CalledProcessError as e:
    print(f"Błąd podczas tworzenia lub usuwania snapshota: {e}")
