# tool_erase.py
# Simple voxel removal tool
# Copyright (c) 2013, Graham R King
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from PySide import QtGui
from tool import Tool

class EraseTool(Tool):

    def __init__(self, parent):
        super(EraseTool, self).__init__(parent)
        # Create our action / icon
        self.action = QtGui.QAction(
            QtGui.QPixmap(":/images/gfx/icons/shovel.png"), 
            "Erase", None)
        self.action.setStatusTip("Erase voxels")
        self.action.setCheckable(True)

    # Clear the targeted voxel
    def on_activate(self, target):
        target.voxels.set(target.x, target.y, target.z, 0)