import Part
from PySide import QtGui
from nodeeditor import BaseNode
from nodeeditor.freecad import slots


class SphereNode(BaseNode):
    """return a sphere with a given radius (float)"""
    def __init__(self, scene):
        super(SphereNode, self).__init__(scene, "sphere")
        self.radius = QtGui.QDoubleSpinBox()
        self.radius.setValue(3)
        self.radius_slot = slots.SlotInput(scene)
        self.shape_out = slots.ShapeOutput(scene)
        self.addWidget(self.radius, self.radius_slot)
        self.addWidget(self.shape_out, QtGui.QLabel('shape'))
        self.shape_out.output = self.output

    def output(self):
        r = self.radius_slot.input() or self.radius.value()
        self.radius.setValue(r)
        return Part.makeSphere(r)


class CylinderNode(BaseNode):
    """return a cylinder with given height and radius"""
    def __init__(self, scene):
        super(CylinderNode, self).__init__(scene, "cylinder")
        self.height = QtGui.QDoubleSpinBox()
        self.height.setValue(10.)
        self.height_slot = slots.SlotInput(scene)
        self.radius = QtGui.QDoubleSpinBox()
        self.radius.setValue(3)
        self.radius_slot = slots.SlotInput(scene)
        self.shape_out = slots.ShapeOutput(scene)
        self.addWidget(self.height, self.height_slot)
        self.addWidget(self.radius, self.radius_slot)
        self.addWidget(self.shape_out, QtGui.QLabel('shape'))
        self.shape_out.output = self.output

    def output(self):
        h = self.height_slot.input() or self.height.value()
        r = self.radius_slot.input() or self.radius.value()
        self.height.setValue(h)
        self.radius.setValue(r)
        return Part.makeCylinder(r, h)


ButtonDict = {
    "Sphere": SphereNode,
    "Cylinder": CylinderNode
    }
