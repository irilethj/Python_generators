The emit_gel() generator function should
simulate the measured fluid pressure. It should generate an infinite stream of numbers from
from 0 to 100 (values > 100 are considered an error) with a random step chosen from the range of
[0, step], where step is the argument of the emit_gel() generator.
Second, pressure control guidelines must be followed. The operating pressure should
be between 20 and 80, that is, if the generator at any point produces a value below 20 or above 80
an action must be applied that will change the sign of the step. To implement such a
valve you need to write another function valve(), which will loop through the values of the
emit_gel() and use the .send() method to change the sign of the current step.
Third, you need to implement an emergency shutdown. If the pressure is above 90 or below 10, the generator of the
emit_gel() generator should be gracefully closed and the script should be terminated.