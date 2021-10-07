from geyser import Geyser
from torchvision.transforms import ToTensor

from geyser_lava.utility import unflatten

unflatten('reference', 'root', 'train', 'transform', 'download', name='cifar_unflatten')


@Geyser.functor(provides=('transform',))
def to_tensor():
    return ToTensor(),
