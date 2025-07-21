import json
import os
import shutil
from pathlib import Path
from subprocess import run


MANIFEST = Path("manifest.json")


def delete_resources_for_disabled_features():
    with MANIFEST.open() as manifest_file:
        manifest = json.load(manifest_file)
        for feature in manifest['features']:
            if not feature['enabled']:
                print(f"Removing resources for disabled feature {feature['name']}...")
                for resource in feature['resources']:
                    delete_resource(resource)
    print("Cleanup complete, removing manifest...")
    delete_resource(MANIFEST)


def delete_resource(resource):
    if os.path.isfile(resource):
        print("Removing file: {}".format(resource))
        os.remove(resource)
    elif os.path.isdir(resource):
        print("Removing directory: {}".format(resource))
        shutil.rmtree(resource)


def run_commands():
    run(["git", "init"], check=True)
    run(["pre-commit", "autoupdate"], check=True)


if __name__ == "__main__":
    delete_resources_for_disabled_features()
    run_commands()
