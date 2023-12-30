Calculus 3 Full Course | Calculus 3 complete course

https://www.youtube.com/watch?v=taGq6Vusclo&t=12s

# Introduction to Vectors

**Definition:** A *vector* is a quantity with direction and magnitude
(length), with tail (initial point) and head (terminal point).

Two vectors are considered to be the same (equivalent) if they have the same
direction and the same length.

**Definition:** A *scalar* is a real number. It does not have a direction.

If we place the initial point of a vector $\vec{a}$ at the *origin*, then the
vector can be described by giving the x and y coordinates of the terminal
point.  $\vec{a} = <3,4>$

**Definition:** The *components* of a vector are the x and y coordinates of its
terminal point when its initial point is at the origin.

**Note:** In general, the components of the vector that starts at a point $A =
(x_{1}, y_{1})$ and ends at a point B = $(x_{2}, y_{2})$ are: $<x_{2} - x_{1},
y_{2} - y_{1}>$

###### Properties of vectors
- Addition is commutative
- Addition is associative
- Additive identity
- Additive inverses
- Distributive property for scalars
- associativity of scalar multiplication
- Multiplicative identity

# Vector length and unit vectors

**Definition:** The length of the vector $\vec{w} = < w_{1}, w_{2}, w_{3}>$ is
$\| \vec{w} \| = \sqrt{w_{1}^{2} + w_{2}^{2} + w_{3}^{2}}$

**Definition:** A unit vector is a vector of norm 1.

**Note:** Rescaling a vector to make it a unit vector is called normalizing.

# Dot product

**Definition:** If $\vec{a} = < a_{1}, a_{2}, a_{3} >$ and $\vec{b} = < b_{1},
b_{2}, b_{3} >$, then the dot product is given by: $\vec{a} \cdot \vec{b} =
a_{1} b_{1} + a_{2} b_{2} + a_{3} b_{3}$

# The two definitions of dot product are equivalent

**Definition:** $\vec{a} \cdot \vec{b} = \| \vec{a} \| \| \vec{b} \|
cos(\theta)$

# Cross product

**Definition:** The cross-product of two vectors is given by: $\vec{a} \times
\vec{b} = \vec{i} (a_{2}b_{3} - b_{2}a_{3}) - \vec{j}(a_{1}b_{3} - b_{1}a_{3}) +
\vec{k} (a_{1}b_{2} - b_{1}a_{2})$

##### Properties of Cross Product

- If $\theta$ is the angle between $\vec{a}$ and $\vec{b}$, with $0 \leq \theta
\leq \pi$, then the length of $\vec{a} \times \vec{b}$ is given by $\| \vec{a}
\times \vec{b} \| = \| \vec{a} \| \|\vec{b}\| \sin(\theta)$ 

# Cross product and areas of parallelograms

Area $= \|\vec{a} \times \vec{b}\|$

# Properties of cross product

- $\vec{u} \times \vec{v} = - (\vec{v} \times \vec{u})$
- $(a\vec{u}) \times (b\vec{v}) = ab(\vec{u} \times \vec{v})$
- $\vec{u} \times (\vec{v} + \vec{w}) = (\vec{u} \times \vec{v}) + (\vec{u}
\times \vec{w})$
- $(\vec{u} + \vec{v}) \times \vec{w} = (\vec{u} \times \vec{w}) + (\vec{v}
\times \vec{w})$

# Lines and planes in 3D

The equation of a line through the point $(x_{0}, y_{0}, z_{0})$ in the
direction of the vector <a, b, c> can be described:

##### parametric equations:
- $x = at + x_{0}$
- $y = bt + y_{0}$
- $z = ct + z_{0}$

##### symmetric equations:
- $t = \frac{x - x_{0}}{a} = \frac{y - y_{0}}{b} = \frac{z - z_{0}}{c}$

#### vector equation
- $\vec{r}(t) = < at + x_{0}, bt + y_{0}, ct + z_{0}>$

The plane through the point $(x_{0}, y_{0}, z_{0})$ and perpendicular to the
vector $<a, b, c>$ is given by the equation: 

$a(x - x_{0}) + b(y - y_{0}) + c(z - z_{0}) = 0$

$ax + by + cz = ax_{0} + by_{0} + cz_{0}$

# Vector functions and space curves

**Definition:** A *vector function or *vector-valued function* is a function
whose domain is a set of real numbers and whose range is a set of vectors.

$\vec{r}(t) = <r_{1}(t), r_{2}(t)... r_{n}(t)>$

# Derivatives and integrals of vector functions

**Definition:** The *derivative* of the vector function $\vec{r}(t)$ is the same
thing as the tangent vector, defined as

$\frac{d\vec{r}}{d\vec{t}} = \vec{r}'(t) = \lim_{h\to0} \frac{\vec{r}(t + h) -
\vec{r}(t)}{h}$

If $\vec{r}(t) = <f(t), g(t), h(t)>$, then $\vec{r}'(t) = <f'(t), g'(t), h'(t)>$

The derivative of a vector function is a (circle one) vector/scalar. [tangent
vector]

The *unit tangent vector is*: $\vec{T}(t) = \frac{\vec{r}'(t)}{\| \vec{r}'(t)
\|}$

**Definition:** If $\vec{r}(t) = <f(t), g(t), h(t)>$ then

$\int{\vec{r}(t)dt} = <\int{f(t)dt}, \int{g(t)dt}, \int{h(t)dt}>$

and 

$\int_{a}^{b}{\vec{r}(t)dt} = <\int_{a}^{b}{f(t)dt}, \int_{a}^{b}{g(t)dt},
\int_{a}^{b}{h(t)dt}>$

# Arclenght for parametric curves

$arclenght = \int_a^b{\sqrt{ f'(t)^2 + g'(t)^2 }} dt$

$arclenght = \int_a^b{\sqrt{\frac{dx}{dt}^2 + \frac{dy}{dt}^2}} dt$

# Functions of several variables

**Definition:** A function $f$ of two variables is a rule that assigns to each
ordered pair of real numbers $(x, y)$ in a set $D$ a unique real number denoted
by $f(x, y)$ [or $z$].
The set D is the *domain* of $f$.
The *range* of $f$ is ${z = f(x,y) | (x,y) in D}$.
x and y are *independent variables*.
z is the *dependent variable*.

The graph of $f$ is the set of all points (x, y, z) in $R^3$ such that $z =
f(x, y)$ and $(x, y)$ is in $D$.
