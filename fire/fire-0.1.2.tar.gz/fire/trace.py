# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module has classes for tracing the execution of a Fire execution.

A FireTrace consists of a sequence of FireTraceElement objects. Each element
represents an action taken by Fire during a single Fire execution. An action may
be instantiating a class, calling a routine, or accessing a property.

Each action consumes args and results in a new component. The final component
is serialized to stdout by Fire as well as returned by the Fire method. If
a Fire usage error occurs, such as insufficient arguments being provided to call
a function, then that error will be captured in the trace and the final
component will be None.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pipes

INITIAL_COMPONENT = 'Initial component'
INSTANTIATED_CLASS = 'Instantiated class'
CALLED_ROUTINE = 'Called routine'
ACCESSED_PROPERTY = 'Accessed property'
COMPLETION_SCRIPT = 'Generated completion script'
INTERACTIVE_MODE = 'Entered interactive mode'


class FireTrace(object):
  """A FireTrace represents the steps taken during a single Fire execution.

  A FireTrace consists of a sequence of FireTraceElement objects. Each element
  represents an action taken by Fire during a single Fire execution. An action
  may be instantiating a class, calling a routine, or accessing a property.
  """

  def __init__(self, initial_component, name=None, separator='-', verbose=False,
               show_help=False, show_trace=False):
    initial_trace_element = FireTraceElement(
        component=initial_component,
        action=INITIAL_COMPONENT,
    )

    self.name = name
    self.separator = separator
    self.elements = [initial_trace_element]
    self.verbose = verbose
    self.show_help = show_help
    self.show_trace = show_trace

  def GetResult(self):
    """Returns the component from the last element of the trace."""
    return self.GetLastHealthyElement().component

  def GetLastHealthyElement(self):
    """Returns the last element of the trace that is not an error.

    This element will contain the final component indicated by the trace.

    Returns:
      The last element of the trace that is not an error.
    """
    for element in reversed(self.elements):
      if not element.HasError():
        return element

  def HasError(self):
    """Returns whether the Fire execution encountered a Fire usage error."""
    return self.elements[-1].HasError()

  def AddAccessedProperty(self, component, target, args, filename, lineno):
    element = FireTraceElement(
        component=component,
        action=ACCESSED_PROPERTY,
        target=target,
        args=args,
        filename=filename,
        lineno=lineno,
    )
    self.elements.append(element)

  def AddCalledRoutine(self, component, target, args, filename, lineno,
                       capacity):
    """Adds an element to the trace indicating that a routine was called.

    Args:
      component: The result of calling the routine.
      target: The name of the routine.
      args: The args consumed in order to call this routine.
      filename: The file in which the routine is defined, or None if N/A.
      lineno: The line number on which the routine is defined, or None if N/A.
      capacity: (bool) Whether the routine could have accepted additional args.
    """
    element = FireTraceElement(
        component=component,
        action=CALLED_ROUTINE,
        target=target,
        args=args,
        filename=filename,
        lineno=lineno,
        capacity=capacity,
    )
    self.elements.append(element)

  def AddInstantiatedClass(self, component, target, args, filename, lineno,
                           capacity):
    """Adds an element to the trace indicating that a class was instantiated.

    Args:
      component: The result of instantiating the class.
      target: The name of the class.
      args: The args consumed in order to instantiate the class.
      filename: The file in which the class is defined, or None if N/A.
      lineno: The line number on which the class is defined, or None if N/A.
      capacity: (bool) Whether cls.__init__ could have accepted additional args.
    """
    element = FireTraceElement(
        component=component,
        action=INSTANTIATED_CLASS,
        target=target,
        args=args,
        filename=filename,
        lineno=lineno,
        capacity=capacity,
    )
    self.elements.append(element)

  def AddCompletionScript(self, script):
    element = FireTraceElement(
        component=script,
        action=COMPLETION_SCRIPT,
    )
    self.elements.append(element)

  def AddInteractiveMode(self):
    element = FireTraceElement(action=INTERACTIVE_MODE)
    self.elements.append(element)

  def AddError(self, error, args):
    element = FireTraceElement(error=error, args=args)
    self.elements.append(element)

  def AddSeparator(self):
    """Marks that the most recent element of the trace used  a separator.

    A separator is an argument you can pass to a Fire CLI to separate args left
    of the separator from args right of the separator.

    Here's an example to demonstrate the separator. Let's say you have a
    function that takes a variable number of args, and you want to call that
    function, and then upper case the result. Here's how to do it:

    # in Python
    def display(arg1, arg2='!'):
      return arg1 + arg2

    # from Bash (the default separator is the hyphen -)
    display hello   # hello!
    display hello upper # helloupper
    display hello - upper # HELLO!

    Note how the separator caused the display function to be called with the
    default value for arg2.
    """
    self.elements[-1].AddSeparator()

  def _Quote(self, arg):
    if arg.startswith('--') and '=' in arg:
      prefix, value = arg.split('=', 1)
      return pipes.quote(prefix) + '=' + pipes.quote(value)
    return pipes.quote(arg)

  def GetCommand(self):
    """Returns the command representing the trace up to this point.

    Returns:
      A string representing a Fire CLI command that would produce this trace.
    """
    args = []
    if self.name:
      args.append(self.name)

    for element in self.elements:
      if element.HasError():
        continue
      if element.args:
        args.extend(element.args)
      if element.HasSeparator():
        args.append(self.separator)

    if self.NeedsSeparator():
      args.append(self.separator)

    return ' '.join(self._Quote(arg) for arg in args)

  def NeedsSeparator(self):
    """Returns whether a separator should be added to the command.

    If the command is a function call, then adding an additional argument to the
    command sometimes would add an extra arg to the function call, and sometimes
    would add an arg acting on the result of the function call.

    This function tells us whether we should add a separator to the command
    before adding additional arguments in order to make sure the arg is applied
    to the result of the function call, and not the function call itself.

    Returns:
      Whether a separator should be added to the command if order to keep the
      component referred to by the command the same when adding additional args.
    """
    element = self.GetLastHealthyElement()
    return element.HasCapacity() and not element.HasSeparator()

  def __str__(self):
    return '\n'.join(
        '{index}. {trace_string}'.format(
            index=index + 1,
            trace_string=element,
        )
        for index, element in enumerate(self.elements)
    )


class FireTraceElement(object):
  """A FireTraceElement represents a single step taken by a Fire execution.

  Examples of a FireTraceElement are the instantiation of a class or the
  accessing of an object member.
  """

  def __init__(self,
               component=None,
               action=None,
               target=None,
               args=None,
               filename=None,
               lineno=None,
               error=None,
               capacity=None):
    """Instantiates a FireTraceElement.

    Args:
      component: The result of this element of the trace.
      action: The type of action (eg instantiating a class) taking place.
      target: (string) The name of the component being acted upon.
      args: The args consumed by the represented action.
      filename: The file in which the action is defined, or None if N/A.
      lineno: The line number on which the action is defined, or None if N/A.
      error: The error represented by the action, or None if N/A.
      capacity: (bool) Whether the action could have accepted additional args.
    """
    self.component = component
    self._action = action
    self._target = target
    self.args = args
    self._filename = filename
    self._lineno = lineno
    self._error = error
    self._separator = False
    self._capacity = capacity

  def HasError(self):
    return self._error is not None

  def HasCapacity(self):
    return self._capacity

  def HasSeparator(self):
    return self._separator

  def AddSeparator(self):
    self._separator = True

  def __str__(self):
    if not self.HasError():
      # Format is: {action} "{target}" ({filename}:{lineno})
      string = self._action
      if self._target is not None:
        string += ' "{target}"'.format(target=self._target)
      if self._filename is not None:
        path = self._filename
        if self._lineno is not None:
          path += ':{lineno}'.format(lineno=self._lineno)

        string += ' ({path})'.format(path=path)
      return string
    else:
      return str(self._error)
