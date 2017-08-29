## Filename    : charter.py
## Author(s)   : Geoffroy Andrieux
## Created     : 03/2010
## Revision    :
## Source      :
##
## Copyright 2012 : IRISA/IRSET
##
## This library is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published
## by the Free Software Foundation; either version 2.1 of the License, or
## any later version.
##
## This library is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY, WITHOUT EVEN THE IMPLIED WARRANTY OF
## MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.  The software and
## documentation provided here under is on an "as is" basis, and IRISA has
## no obligations to provide maintenance, support, updates, enhancements
## or modifications.
## In no event shall IRISA be liable to any party for direct, indirect,
## special, incidental or consequential damages, including lost profits,
## arising out of the use of this software and its documentation, even if
## IRISA have been advised of the possibility of such damage.  See
## the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this library; if not, write to the Free Software Foundation,
## Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
##
## The original code contained here was initially developed by:
##
##     Geoffroy Andrieux.
##     IRISA
##     Symbiose team
##     IRISA  Campus de Beaulieu
##     35042 RENNES Cedex, FRANCE
##
##
## Contributor(s): Michel Le Borgne
##
"""
Small widgets for Cadbiom gui
"""
import gtk
import re

from utils.listDisplay import ToggleList
from cadbiom.models.guard_transitions.analyser.ana_visitors import FrontierVisitor
from utils.warn import cancel_warn
from cadbiom.models.guard_transitions.chart_model import ChartModel

from utils.fileHandling import FileChooser
from utils.reporter import CompilReporter
from cadbiom.models.guard_transitions.translators.chart_xml_pid import \
            MakeModelFromPidFile
from chart_simulator.chart_simul_controler import DisplayError

import pkg_resources

class SearchManager(object):
    """
    List of simple nodes for searching
    """
    def __init__(self, chart, notebook, label):
        self.charter = chart
        self.model = None
        self.model_changed = True
        self.notebook = notebook

        # simple nodes
        sn_frame = gtk.Frame()
        self.sn_frame = sn_frame
        vbox = gtk.VBox(False, 0)
        sn_frame.add(vbox)
        # simple nodes list
        self.sn_viewer = ToggleList()
        label = gtk.Label(label)
        # wrap into scrollwindow
        scroll = gtk.ScrolledWindow()
        scroll.add_with_viewport(self.sn_viewer)
        vbox.pack_start(scroll, True, True, 0)
        # buttons
        hbox = gtk.HBox()
        vbox.pack_start(hbox, False, False, 0)
        but = gtk.Button('Update')
        but.connect("clicked", self.on_update)
        self.show_but = but
        hbox.pack_start(but, False, False, 0)
        but = gtk.Button('Show')
        but.connect("clicked", self.on_show)
        self.show_but = but
        hbox.pack_start(but, False, False, 0)
        but = gtk.Button('Extract')
        but.connect("clicked", self.on_extract)
        self.show_but = but
        hbox.pack_start(but, False, False, 0)
        but = gtk.Button('Clear')
        but.connect("clicked", self.on_clear)
        self.clear_but = but
        hbox.pack_start(but, False, False, 0)
        notebook.append_page(sn_frame, label)
        # entry
        self.entry = gtk.Entry()
        vbox.pack_start(self.entry, False, False, 0)

    def update(self):
        """
        As it says
        """
        self.model_changed = True

    def set_model(self, model):
        """
        As it says
        """
        if self.model:
            self.model.detach(self)
        self.model = model
        self.model.attach(self)
        self.model_changed = False
        # get node names
        lnode = model.get_simple_node_names()
        lnode.sort()
        # display node names
        self.sn_viewer.refresh(lnode)

    def on_clear(self, widget):
        """
        clear button callback
        """
        self.sn_viewer.clear(widget)
        self.entry.set_text('')
        if self.model:
            self.model.search_unmark()
            self.model_changed = False # search_mark implies a notify

    def on_update(self, widget):
        """
        update button callback
        """
        if self.model:
            self.model.search_unmark()
            # get node names
            lnode = self.model.get_simple_node_names()
            lnode.sort()
            # display node names
            self.sn_viewer.refresh(lnode)
            self.model_changed = False

    def on_show(self, widget):
        """
        show button callback
        """
        if not self.model:
            return
        # check model
        if self.model_changed:
            cancel_warn("Model is modified: update?")
        # mark nodes and show
        lnode = self.sn_viewer.get_selected_items()
        if lnode == []:
            regex = self.entry.get_text()
            if len(regex) == 0:
                return
            try:
                regex_obj = re.compile(regex)
            except:
                cancel_warn("Incorrect regular expression")
                return
            lnode = self.model.get_matching_node_names(regex_obj)

        self.model.search_mark(lnode)
        self.model_changed = False # search_mark implies a notify

    def on_extract(self, widget):
        """
        extract node environment
        """
        if not self.model:
            return
        # check model
        if self.model_changed:
            cancel_warn("Model is modified: update?")
        # mark nodes and show
        lnode_n = self.sn_viewer.get_selected_items()
        if lnode_n == []:
            regex = self.entry.get_text()
            if len(regex)==0:
                return
            try:
                regex_obj = re.compile(regex)
            except:
                cancel_warn("Incorrect regular expression")
                return
            lnode_n = self.model.get_matching_node_names(regex_obj)

        submodel = ChartModel(self.model.name + "_extract")
        tnode = submodel.get_root()
        for node_n in lnode_n:
            # avoid double node declaration
            try:
                extn = submodel.node_dict[node_n]
                break
            except:
                node = self.model.node_dict[node_n]
                nsn = tnode.add_copy(node)
            extn = self.model.node_dict[node_n]
            # incoming and out going transitions except with start or trap
            for trans in extn.incoming_trans:
                ori_n = trans.ori.name
                try:
                    ori = submodel.node_dict[ori_n]
                except:
                    ori = tnode.add_copy(trans.ori)
                ntr = tnode.add_transition(ori, nsn)
                if ntr:
                    ntr.set_condition(trans.condition)
                    ntr.set_event(trans.event)
                    ntr.set_action(trans.action)
            for trans in extn.outgoing_trans:
                ext_n = trans.ext.name
                try:
                    target = submodel.node_dict[ext_n]
                except:
                    target = tnode.add_copy(trans.ext)
                ntr = tnode.add_transition(nsn, target)
                if ntr:
                    ntr.set_condition(trans.condition)
                    ntr.set_event(trans.event)
                    ntr.set_action(trans.action)
            # transitions conditioned by node
            try:
                trl = self.model.signal_transition_dict[node]
            except:
                trl = []
            for trans in trl:
                ori_n = trans.ori.name
                try:
                    ori = submodel.node_dict[ori_n]
                except:
                    ori = tnode.add_copy(trans.ori)
                ext_n = trans.ext.name
                try:
                    target = submodel.node_dict[ext_n]
                except:
                    target = tnode.add_copy(trans.ext)
                ntr = tnode.add_transition(ori, target)
                if ntr:
                    ntr.set_condition(trans.condition)
                    ntr.set_event(trans.event)
                    ntr.set_action(trans.action)
        # display in charter
        self.charter.add_edit_mvc(submodel.name, submodel, False)
        self.charter.do_layout(None, "hierarchical_LR")

    def get_selected_keywords(self):
        """
        As it says
        """
        return self.sn_viewer.get_selected_items()

    def clear(self):
        """
        It is clear
        """
        self.sn_viewer.refresh([])

class SearchFrontier(SearchManager):
    """
    Same as SearchManager but specialized on frontier nodes
    """
    def __init__(self, chart, notebook, label):
        SearchManager.__init__(self, chart, notebook, label)

    def set_model(self, model):
        """
        As it says
        """
        if self.model:
            self.model.detach(self)
        self.model = model
        self.model.attach(self)
        self.model_changed = False
        # get node names
        lnode = self.get_frontier_node_names()
        lnode.sort()
        # display node names
        self.sn_viewer.refresh(lnode)

    def on_update(self, widget):
        self.model.search_unmark()
        # get node names
        lnode = self.get_frontier_node_names()
        lnode.sort()
        # display node names
        self.sn_viewer.refresh(lnode)
        self.model_changed = False

    def get_frontier_node_names(self):
        """
        As it says
        """
        fvi = FrontierVisitor()
        self.model.accept(fvi)
        return fvi.frontier

    def clear(self):
        self.sn_viewer.refresh([])



class LegendWindow(object):
    """
    Widget to display the legend
    """
    def __init__(self, parent=None):

        self.win = gtk.Window()
        self.win.set_title("CADBIOM-Chart Legend")
        self.win.set_position(gtk.WIN_POS_CENTER)
        self.win.connect("destroy", self.on_destroy)
        image = gtk.Image()
        image.set_from_file("cadbiom_gui/gt_gui/legend.png")
        image.show()

        self.win.add(image)
        self.win.show_all()
        # register itself for parent or emvc
        if parent:
            parent.win_register(self)

        self.parent = parent

    def on_destroy(self, widget):
        """
        standard destroy callback
        """
        if self.parent:
            self.parent.win_remove(self)

    def destroy(self):
        """
        if registered as a child
        """
        if self.win:
            self.win.destroy()

class ImportParam(object):
    """
    Widget for model importing
    """
    def __init__(self, chart):
        self.charter = chart

        # window creation
        template = pkg_resources.resource_filename(
            __name__,
            "chart_glade/import_parameter.glade"
        )
        self.wtree = gtk.glade.XML(template)
        self.main_window = self.wtree.get_widget("window1")
        self.main_window.set_title("Import window")

        self.main_window.set_resizable(True)
        hei = gtk.gdk.screen_height()
        hei = int(hei * 0.20)
        self.main_window.set_size_request(350, hei)

        if (self.main_window):
            self.main_window.connect("destroy", self.on_destroy)

        self.main_window.set_position(gtk.WIN_POS_CENTER)

        # init param
        self.ai_inter = 0
        self.has_clock = False

        # interpretation radio button
        rbut = self.wtree.get_widget("or_rb")
        rb_name = rbut.get_name()
        rbut.connect("toggled", self.ai_inter_rb_callback, rb_name)

        rbut = self.wtree.get_widget("and_rb")
        rb_name = rbut.get_name()
        rbut.connect("toggled", self.ai_inter_rb_callback, rb_name)

        # Uncomment to add new buttons
#        rb = self.wtree.get_widget("or_and_rb")
#        rb_name = rb.get_name()
#        rb.connect("toggled", self.ai_inter_rb_callback, rb_name)
#
#        rb = self.wtree.get_widget("and_or_rb")
#        rb_name = rb.get_name()
#        rb.connect("toggled", self.ai_inter_rb_callback, rb_name)

        # clock radio button
        rbut = self.wtree.get_widget("withoutClock_rb")
        rbut.connect("toggled", self.clock_rb_callback, False)

        rbut = self.wtree.get_widget("withClock_rb")
        rbut.connect("toggled", self.clock_rb_callback, True)

        # import button
        button = self.wtree.get_widget("importButton")
        button.connect("clicked", self.on_import)

        # display
        self.main_window.show_all()

    def ai_inter_rb_callback(self, widget, ai_name):
        """
        set activator/inhibitor interpretation (and or or)
        """
        if ai_name == "or_rb":
            self.ai_inter = 0
        elif ai_name == "and_rb":
            self.ai_inter = 1

        # Uncomment to add new buttons
#        elif ai_name == "or_and_rb":
#            self.ai_inter = 2
#        else :
#            self.ai_inter = 3

    def clock_rb_callback(self, widget, has_clock):
        """
        set clock generation
        """
        if has_clock :
            self.has_clock = True
        else :
            self.has_clock = False

    def on_import(self, widget):
        """
        lauch import
        """
        fch = FileChooser("Import from PID xml", "xml files", "*.xml")
        fch.do_action(self.import_from_pid_file)

    def import_from_pid_file(self, file):
        """
        compile a pid file
        """
        crep = CompilReporter()
        parser = MakeModelFromPidFile(file, crep,
                                          self.has_clock, self.ai_inter)
        if crep.error :
            DisplayError(crep, parser.model.name)
        else :
            model = parser.model
            model.modified = False
            self.charter.add_edit_mvc(model.name, model)
            self.destroy()

    def on_destroy(self, widget):
        """
        standard destroy callback
        """
        if self.main_window:
            self.main_window.destroy()

    def destroy(self):
        """
        for parents
        """
        self.on_destroy(None)


