# tool_shade.py
# Left click to darken voxel. Right click to lighten voxel.
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
from tool import Tool, EventData, MouseButtons, KeyModifiers, Face
from plugin_api import register_plugin


class ShaderTool(Tool):

    def __init__(self, api):
        super(ShaderTool, self).__init__(api)
        # Create our action / icon
        self.action = QtGui.QAction(
            QtGui.QPixmap(":/images/gfx/icons/Shade.png"),
            "Lighten/Darken", None)
        self.action.setStatusTip("Adjust voxel darkness a little.")
        self.action.setCheckable(True)
        self.action.setShortcut(QtGui.QKeySequence("Ctrl+8"))
        # Register the tool
        self.api.register_tool(self)

    # Color the targeted voxel
    def on_mouse_click(self, data):
        # If we have a voxel at the target, get its color.
        voxel = data.voxels.get(data.world_x, data.world_y, data.world_z)
        if voxel:
            self.api.set_palette_color(voxel)
            if data.mouse_button == MouseButtons.LEFT:
                # Darken the color.
                newColor = self.api.get_palette_color().darker(110)
                # set the voxel's new color.
                data.voxels.set(data.world_x, data.world_y, data.world_z, newColor)
            elif data.mouse_button == MouseButtons.RIGHT:
                # Lighten the color.
                newColor = self.api.get_palette_color().lighter(110)
                # set the voxel's new color.
                data.voxels.set(data.world_x, data.world_y, data.world_z, newColor)

    # Color when dragging also
    def on_drag(self, data):
        self.on_mouse_click(data)

register_plugin(ShaderTool, "Shadeing Tool", "1.0")
