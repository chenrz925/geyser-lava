from geyser import Geyser


@Geyser.functor(requires=('path',))
def utility_path_validator(path, **kwargs):
    assert hasattr(path, 'temporary')
    assert hasattr(path, 'home')
    assert hasattr(path, 'current')


@Geyser.functor(requires=('env',))
def utility_env_validator(env, **kwargs):
    assert 'TEST' in env
    assert env['TEST'] == 'TEST'


@Geyser.functor(requires=('id',))
def utility_id_validator(id, **kwargs):
    assert 'TEST' in id


class TestTaskUtility(object):
    def test_ultility_path_provider(self):
        Geyser._build_context({
            'tasks': [
                {
                    'reference': 'geyser_lava.task.utility.PathProvider',
                    'name': 'path',
                    'type': 'task'
                }
            ],
            'flow': {
                'name': 'root',
                'type': 'linear',
                'include': ['path']
            },
            'engine': 'serial',
        })()

    def test_ultility_path_provider_validator(self):
        Geyser._build_context({
            'tasks': [
                {
                    'reference': 'geyser_lava.task.utility.PathProvider',
                    'name': 'path',
                    'type': 'task'
                },
                {
                    'reference': 'tests.test_task_ultility.UtilityPathValidator',
                    'name': 'validator',
                    'type': 'functor',
                    'rebind': {
                        'path': 'path_provider'
                    }
                }
            ],
            'flow': {
                'name': 'root',
                'type': 'linear',
                'include': ['path', 'validator']
            },
            'engine': 'serial',
        })()

    def test_ultility_env(self):
        Geyser._build_context({
            'tasks': [
                {
                    'reference': 'geyser_lava.task.utility.EnvProvider',
                    'name': 'env',
                    'type': 'task',
                    'inject': {
                        'TEST': 'TEST'
                    }
                },
                {
                    'reference': 'tests.test_task_ultility.UtilityEnvValidator',
                    'name': 'validator',
                    'type': 'functor',
                }
            ],
            'flow': {
                'name': 'root',
                'type': 'linear',
                'include': ['env', 'validator']
            },
            'engine': 'serial',
        })()

    def test_utility_id(self):
        Geyser._build_context({
            'tasks': [
                {
                    'reference': 'geyser_lava.task.utility.IdProvider',
                    'name': 'id',
                    'type': 'task',
                },
                {
                    'reference': 'tests.test_task_ultility.UtilityIdValidator',
                    'name': 'validator',
                    'type': 'functor',
                }
            ],
            'flow': {
                'name': 'root',
                'type': 'linear',
                'include': ['id', 'validator']
            },
            'engine': 'serial',
            'inject': {
                'title': 'TEST'
            }
        })()
