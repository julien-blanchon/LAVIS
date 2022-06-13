from lavis.common.registry import registry
from lavis.datasets.builders.base_dataset_builder import BaseDatasetBuilder


@registry.register_builder("flickr30k")
class Flickr30kBuilder(BaseDatasetBuilder):
    def __init__(self, cfg=None):
        super().__init__(cfg)

    @classmethod
    def default_config_path(cls, type="default"):
        paths = {"default": "lavis/configs/datasets/flickr30k/defaults.yaml"}

        return paths[type]

    def _download_vis(self):
        pass