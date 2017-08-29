from infra_buddy.aws.ecs import ECSBuddy
from infra_buddy.deploy.deploy import Deploy
from infra_buddy.utility import print_utility


class ECSDeploy(Deploy):
    def __init__(self, artifact_id, artifact_location, deploy_ctx):
        super(ECSDeploy, self).__init__(deploy_ctx)
        self.artifact_id = artifact_id
        self.artifact_location = artifact_location

    def _internal_deploy(self, dry_run):

        ecs_buddy = ECSBuddy(self.deploy_ctx)
        ecs_buddy.set_container_image(self.artifact_location, self.artifact_id)
        if dry_run:
            print_utility.warn("ECS Deploy would update service {} to use image {}".format(ecs_buddy.ecs_service,ecs_buddy.new_image))
            return
        if ecs_buddy.requires_update():
            ecs_buddy.perform_update()
        else:
            print_utility.info("ECS using already using image - "
                               "{artifact_location}:{artifact_id}".
                               format(artifact_location=self.artifact_location,
                                      artifact_id=self.artifact_id))
