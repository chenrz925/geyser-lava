from geyser import Geyser

from geyser_lava.utility import flatten, unflatten

flatten('a', 'b', ('c', ('a', 'b')), name='test_flatten')
unflatten('a', 'b', 'c', name='test_unflatten')

@Geyser.functor(requires=('a', 'b', 'c_a', 'c_b'))
def access_inject(a, b, c_a, c_b):
    assert a == 0
    assert b == 0
    assert c_a == 1
    assert c_b == 1

class TestUtility(object):
    def test_unflatten(self):
        Geyser._build_context({
            'tasks': [
                {
                    'reference': 'tests.test_utility.TestFlatten',
                    'name': 'flatten',
                    'type': 'functor',
                    'inject': {
                        'a': 0, 
                        'b': 0
                    }
                },
                {
                    'reference': 'tests.test_utility.AccessInject',
                    'name': 'access',
                    'type': 'functor'
                }
            ],
            'flow': {
                'name': 'root',
                'type': 'linear',
                'include': ['flatten', 'access']
            },
            'engine': 'serial',
            'inject': {
                'c': {
                    'a': 1, 
                    'b': 1
                }
            }
        })()
