from geyser import Geyser


class TestTaskTorchCommon(object):
    def test_dataloader_provider(self):
        Geyser._build_context({
            'tasks': [
                {
                    'reference': 'geyser_lava.task.torch.common.DataLoaderProvider',
                    'name': 'loader',
                    'type': 'task',
                    'inject': {
                        'dataset_params': {
                            'reference': 'torchvision.datasets.mnist.MNIST',
                            'root': 'geyser/test/datasets/mnist',
                            'train': True,
                            'download': True
                        },
                        'loader_params': {
                            'batch_size': 128,
                            'shuffle': True
                        }
                    }
                }
            ],
            'flow': {
                'name': 'root',
                'type': 'linear',
                'include': ['loader']
            },
            'engine': 'serial',
        })()

    def test_model_provider(self):
        Geyser._build_context({
            'tasks': [
                {
                    'reference': 'geyser_lava.task.torch.common.ModelProvider',
                    'name': 'model',
                    'type': 'task',
                    'inject': {
                        'model_params': {
                            'reference': 'torch.nn.modules.conv.Conv2d',
                            'in_channels': 3,
                            'out_channels': 3,
                            'kernel_size': 3
                        }
                    }
                }
            ],
            'flow': {
                'name': 'root',
                'type': 'linear',
                'include': ['model']
            },
            'engine': 'serial',
        })()

    def test_loss_provider(self):
        Geyser._build_context({
            'tasks': [
                {
                    'reference': 'geyser_lava.task.torch.common.LossProvider',
                    'name': 'loss',
                    'type': 'task',
                    'inject': {
                        'loss_params': {
                            'reference': 'torch.nn.modules.loss.CrossEntropyLoss',
                            'inplace': True
                        }
                    }
                }
            ],
            'flow': {
                'name': 'root',
                'type': 'linear',
                'include': ['loss']
            },
            'engine': 'serial',
        })

    def test_optimizer_provider(self):
        Geyser._build_context({
            'tasks': [
                {
                    'reference': 'geyser_lava.task.torch.common.ModelProvider',
                    'name': 'model',
                    'type': 'task',
                    'inject': {
                        'model_params': {
                            'reference': 'torch.nn.modules.conv.Conv2d',
                            'in_channels': 3,
                            'out_channels': 3,
                            'kernel_size': 3
                        }
                    }
                },
                {
                    'reference': 'geyser_lava.task.torch.common.OptimizerProvider',
                    'name': 'optimizer',
                    'type': 'task',
                    'inject': {
                        'optimizer_params': {
                            'reference': 'torch.optim.adam.Adam',
                            'lr': 1e-4
                        }
                    }
                }
            ],
            'flow': {
                'name': 'root',
                'type': 'linear',
                'include': ['model', 'optimizer']
            },
            'engine': 'serial'
        })
