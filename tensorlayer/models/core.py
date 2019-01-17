import tensorflow as tf


class Model():
    """The :class:`Model` class represents a neural network.

    Parameters
    -----------
    inputs : a Layer or list of Layer
        The input(s) to the model.
    outputs : a Layer or list of Layer
        The output(s) to the model.
    name : None or str
        The name of the model.
    """

    @property
    def inputs(self):
        return self._inputs

    @property
    def outputs(self):
        return self._outputs

    def __init__(self, inputs=None, outputs=None, name=None):
        # Model properties
        self.name = name

        # Model inputs and outputs
        # TODO: check type of inputs and outputs
        self._inputs = inputs
        self._outputs = outputs

        # Model state: train or test
        # self.is_train = is_train

    def __call__(self, inputs, is_train):
        # TODO: check inputs corresponds with self._inputs
        results = list()
        for out in self._outputs:
            stacked_layers = list()
            current = out
            # TODO: if inputs is not Input but BaseLayer?
            while current is not None:
                stacked_layers.append(current)
                current = current._input_layer
            # FIXME: assume there is only one inputs
            z = inputs
            for layer in stacked_layers[::-1]:
                z = layer.forward(z, is_train)
            results.append(z)
        return results

    def __str__(self):
        return "  {} ({}) outputs_shape: {}".format(
            self.__class__.__name__, self.name, [tuple(['batch_size'] + o._outputs_shape[1:]) for o in self.outputs]
        )  #_outputs_shape)#outputs.get_shape().as_list())

    ## raise Exceptions for old version codes
    def count_params(self, **kwargs):
        raise Exception("please change count_params --> count_weights")

    def print_params(self, **kwargs):
        raise Exception("please change print_params --> print_weights")

    @property
    def all_params(self):
        raise Exception("please change all_params --> weights")

    @property
    def all_drop(self):
        raise Exception("all_drop is deprecated")