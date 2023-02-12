Analytic Solutions      {#analyticsols}
==================


\tableofcontents


\section separationofvars Method: separation of variables


Separation of variables is a general method of solving partial differential equations. (Others include integral transform methods - see later - and Green's function methods.) The approach we take is to try to keep the independent variables as separate as possible. Usually, separation of variables transforms a PDE in @f$ n @f$ dimensions into @f$ n @f$ ODEs, which are more easily solved.

For the planar-geometry, homogeneous diffusion equation with constant diffusion coefficient, @f$ D @f$:

\f[
    \frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial x^2}
\f]

substitute a separable-variable solution:

\f[
    u(x,t) = X(x)T(t)
\f]

giving:

\f[
    X(x)\frac{\partial T}{\partial t} = D T(t)\frac{\partial^2 X}{\partial x^2}
\f]

This can also be written more simply as:

\f[
    XT' = DTX''
\f]

where the prime represents the ordinary derivative of the function with respect to the independent variable on which it depends.

Dividing through by @f$ u = XT @f$ gives:

\f[
    \frac{T'}{T} = D \frac{X''}{X} = -\lambda
\f]

Each of the terms is a function of only one independent variable. In this example, the left-hand side is a function of @f$ t @f$ only and the right-hand side a function of @f$ x @f$ only, and yet the two terms are equal. This can only be the case if both terms are actually equal to a constant, which we have denoted @f$ -\lambda @f$ (the negative sign is for convenience, which will become clear later).

Using this conclusion, we can arrive at two _ordinary_ differential equations:

\f{gather*}
    T' = -\lambda T \\[10pt]
    -DX'' = \lambda X
\f}

each of which is linear, inhomogeneous, and easy to solve.

The first ODE, which is equivalent to the equation describing radioactive decay:
\f[
    T' = -\lambda T
\f]

with a decay constant @f$ \lambda @f$, has a simple solution:

\f[
    \setlength{\fboxsep}{2.5\fboxsep}
    \boxed{
        T(t) = T(0) \exp(-\lambda t)
    }
\f]

Note that, substituting this back into the definition of the separable-variable solution:

\f[
    u(x,t) = X(x)T(0) \exp(-\lambda t)
\f]

and specifying an arbitrary initial condition:

\f[
    u(x,0) = X(x)T(0) = \varphi(x)
\f]

gives:

\f[
    u(x,t) = \varphi(x) \exp(-\lambda t)
\f]

That is, we can see the behaviour of the overall solution will be for the initial condition, @f$ \varphi(x) @f$, to decay exponentially, with time constant @f$ \lambda @f$.

Now consider the second ODE, governing the spatially-dependent part of the solution:

\f[
    -DX'' = \lambda X
\f]

We can see from the form of this equation that the constant, @f$ \lambda @f$, is an _eigenvalue_ of the linear differential operator @f$ \mathcal{L} = -D\dfrac{d^2}{dx^2} @f$, and corresponds to the _eigenfunction_ @f$ X(x) @f$. In fact, in general, there will be a set of eigenvalues, @f$ \lambda_i @f$, corresponding to eigenfunctions @f$ X_i(x) @f$, and determined by the boundary conditions on @f$ X(x) @f$; and the general solution will be a linear superposition of these.

The general method of solution for a higher-order ODE with constant coefficients is to insert a trial function:

\f[
    X(x) = Ae^{lx}
\f]

giving in this case:

\f[
    -DAl^2e^{lx} = \lambda Ae^{lx}
\f]

simplifying:

\f[
    l^2 = -\dfrac{\lambda}{D}
\f]

The original ODE can be written:

\f[
    X'' = l^2X
\f]

For an @f$N^{\mathrm{th}}@f$-order ODE, this _auxiliary equation_ is an @f$N^{\mathrm{th}}@f$-order polynomial with @f$ N @f$ roots, @f$ l_1, l_2, ..., l_N @f$. The details of the next step depends on whether the roots are real and distinct, repeated, or complex, which correspond to when @f$ \lambda < 0 @f$, @f$ \lambda = 0 @f$, and @f$ \lambda > 0 @f$, respectively.

* If all roots are real and distinct, then the solutions are simply @f$ e^{l_n x}, \; n =1, 2, ..., N  @f$. Since:
  \f[
      l^2 = -\dfrac{\lambda}{D}
  \f]
  this situation arises when @f$ \lambda < 0 @f$ (for physical situations where @f$ D @f$ is non-negative). The roots are:
  \f[
      \arraycolsep=1.4pt
      \begin{array}{lcrcr}
          l_1 &=&  \sqrt{\dfrac{-\lambda}{D}} &=&  \omega \\[10pt]
          l_2 &=& -\sqrt{\dfrac{-\lambda}{D}} &=& -\omega
      \end{array}
  \f]
  I.e. @f$ X_1 = e^{\omega x} @f$ and @f$ X_2 = e^{-\omega x} @f$ are solutions. The superposition @f$ X = c_1 e^{\omega x} + c_2 e^{-\omega x} @f$ gives the general solution.
* If some roots are repeated (e.g. one is repeated @f$ k @f$ times), we have not found @f$ N @f$ linearly-independent solutions, and @f$ k-1 @f$ further solutions are required that are linearly-independent of the existing ones and of each other. By substitution into the original ODE, we can verify that @f$ x_j e^{l_i x} @f$ for @f$ j = 1, 2, ..., k-1 @f$ are such solutions. This situation arises when @f$ \lambda = 0 @f$, and there is only a single unique root (in this second-order case):
  \f[
      l_1 = \sqrt{\dfrac{-\lambda}{D}} = \omega
  \f]
  The solutions are @f$ X_1 = e^{\omega x} @f$ and @f$ X_2 = xe^{\omega x} @f$, and since @f$ \omega = 0 @f$, @f$ X_1 = 1 @f$ and @f$ X_2 = x @f$, and the general solution is @f$ X = c_1 x + c_2 @f$.
* If some of the roots are complex, which is the case if @f$ \lambda > 0 @f$, then each complex root @f$ \alpha + i\beta @f$ has a corresponding root @f$ \alpha - i\beta @f$. For @f$ \lambda > 0 @f$ we find therefore the two roots:
  \f[
      \arraycolsep=1.4pt
      \begin{array}{lcrcr}
          \l_1 &=& i\sqrt{\dfrac{\lambda}{D}} &=& i\omega \\[10pt]
          \l_2 &=& -i\sqrt{\dfrac{\lambda}{D}} &=& -i\omega
      \end{array}
  \f]
  Solutions are @f$ X_1 = e^{i\omega x} @f$ and @f$ X_2 = e^{-i\omega x} @f$, and the general solution is @f$ X = d_1 e^{i\omega x} + d_2 e^{-i\omega x} = c_1 \cos \omega x + c_2 \sin \omega x @f$.

To re-cap, the ODE:
\f[
    -DX'' = \lambda X
\f]

has general solution:

\f[
    \setlength{\fboxsep}{2.5\fboxsep}
    \boxed{
        X(x) =
        \begin{cases}
            c_1 e^{\omega x} + c_2 e^{-\omega x} & \quad \textrm{for} \; \lambda < 0 \\[5pt]
            c_1 x + c_2                          & \quad \textrm{for} \; \lambda = 0 \\[5pt]
            c_1 \cos\omega x + c_2 \sin\omega x  & \quad \textrm{for} \; \lambda > 0
        \end{cases}
    }
\f]


\section finitedomain Finite domain solutions


We shall first consider analytic solutions on a finite interval, because they lead to simpler numerical test problems. (To set up numerical problems that match analytic solutions on an infinite or semi-infinite interval, large numerical domains are necessary so that effects introduced by the edges, which are not present in the analytic solutions, become negligible.)


\subsection zeroboundaries Homogeneous boundary conditions


Consider a situation in which the following boundary conditions are applied:

\f{align}
    u(0,t) &= 0 \nonumber \\[8pt]
    u(L,t) &= 0 \nonumber
\f}

for @f$ t \ge 0 @f$.

First, we apply these boundary conditions to the ODE that describes the spatial dependence:

\f[
    \arraycolsep=1.4pt
    \begin{array}{lcl}
        u(0,t) &= X(0)T(t) &= 0 \\[8pt]
        u(L,t) &= X(L)T(t) &= 0
    \end{array}
\f]

which, since we want non-trivial solutions (@f$T(t) \ne 0 @f$), imply:

\f{align*}
    X(0) &= 0 \\[8pt]
    X(L) &= 0
\f}

Now, for:

\f[
    -DX'' = \lambda X
\f]

we can determine the following.

* For @f$ \lambda < 0 @f$, the solution was:
  \f[
      X(x) = c_1 e^{\lambda x} + c_2 e^{\lambda x}
  \f]
  Applying the boundary conditions we see that:
  \f{gather*}
      c_1 + c_2 = 0 \\[8pt]
      c_1 e^{\omega L} + c_2 e^{-\omega L} = 0
  \f}
  from which we infer that @f$ c_1 = c_2 = 0 @f$, so only trivial solutions exist.
* For @f$ \lambda = 0 @f$:
  \f[
      X(x) = c_1 x + c_2
  \f]
  Applying the boundary conditions:
  \f{gather*}
      c_2 = 0 \\[8pt]
      c_1 L = 0
  \f}
  from which, again, we can see that @f$ c_1 = c_2 = 0 @f$.
* Finally, for @f$ \lambda > 0 @f$:
  \f[
      X(x) = c_1 \cos\omega x + c_2 \sin\omega x
  \f]
  Applying the boundary conditions:
  \f{gather*}
      c_1 = 0 \\[8pt]
      c_2 \sin\omega L = 0
  \f}
  from which we infer that non-zero values of @f$ c_2 @f$ can occur when @f$ \omega L = n\pi @f$, @f$ n @f$ being an integer.

Hence @f$ \lambda > 0 @f$ is the only situation of interest; @f$ \lambda \le 0 @f$ yields only the trivial solution @f$ X(x) = 0 @f$. Therefore we have the following eigenfunctions:

\f[
    X_n(x) = c_2 \sin\left(\dfrac{n\pi}{L}x\right)
\f]

and eigenvalues:

\f[
    \lambda_n = D\left(\dfrac{n\pi}{L}\right)^2
\f]

for @f$ n = 1, 2, ... @f$. For each @f$ \lambda_n @f$, we also have a solution for the time-dependent part:

\f[
    T_n(t) = T(0) \exp{\left(-D\dfrac{n^2\pi^2}{L^2}t\right)}
\f]

These are the general solutions to the two separated ODEs. We can substitute them into the assumed form for the solution to the diffusion equation, which is @f$ u = XT @f$:

\f[
    u_n(x,t) = b_n \sin \left(\frac{n\pi}{L}x \right) \exp\left(-D\frac{n^2\pi^2}{L^2}t\right)
\f]

Every value of @f$ n @f$ is a solution, hence there is a set of solutions, and we can use superposition to find a more general solution:

\f[
    u(x,t) = \sum_{n=1}^{\infty} c_n u_n(x,t)
           = \sum_{n=1}^{\infty} A_n \sin \left( \frac{n\pi}{L}x \right) \exp\left(-D\frac{n^2\pi^2}{L^2}t\right)
\f]

To find the constants @f$ A_n @f$, use the initial condition:

\f[
    u(x,0) = \varphi (x)
\f]

hence:

\f[
    \sum_{n=1}^{\infty} A_n \sin\left(\frac{n\pi}{L}x\right) = \varphi(x)
\f]

We can now use knowledge of Fourier series to determine the coefficients. Multiplying through by @f$ \sin \left(\dfrac{m\pi}{L}x\right) @f$ and then integrating between @f$ 0 @f$ and @f$ L @f$ gives:

\f[
    \int_0^L \sum_{n=1}^{\infty} A_n \sin\left(\frac{n\pi}{L}x\right)\sin\left(\frac{m\pi}{L}x\right) dx = \int_0^L \varphi(x)\sin\left(\frac{m\pi}{L}x\right) dx
\f]

Reversing the order of summation and integration:

\f[
    \sum_{n=1}^{\infty} A_n \int_0^L \sin\left(\frac{n\pi}{L}x\right)\sin\left(\frac{m\pi}{L}x\right) dx = \int_0^L \varphi(x)\sin\left(\frac{m\pi}{L}x\right) dx
\f]

Using the rules of orthogonality, all the terms in the series on the left-hand side disappear, except when @f$ m = n @f$:

\f{gather*}
    A_n \int_0^L \sin\left(\frac{n\pi}{L}x\right)\sin\left(\frac{n\pi}{L}x\right) dx = \int_0^L \varphi(x)\sin\left(\frac{n\pi}{L}x\right) dx \\[8pt]
    A_n \frac{L}{2} = \int_0^L \varphi(x)\sin\left(\frac{n\pi}{L}x\right) dx
\f}

Therefore:
\f[
    A_n = \frac{2}{L} \int_0^L \varphi(x) \sin \left( \frac{n\pi}{L}x\right) dx
\f]

Finally therefore, we have for fixed, zero boundary temperatures and initial distribution @f$ \varphi(x) @f$ the solution:
\f{gather*}
    u(x,t) = \sum_{n=1}^{\infty} A_n \sin \left( \frac{n\pi}{L}x\right) \exp\left(-D\frac{n^2\pi^2}{L^2}t\right) \\[8pt]
    A_n = \frac{2}{L} \int_0^L \varphi(x) \sin \left( \frac{n\pi}{L}x\right) dx
\f}


\subsubsection sininitcon Sinusoidal initial condition (test problems 1, 2, 15, 17)


Perhaps the simplest initial condition is a single sinusoidal function:

\f[
    \varphi(x) = A \sin{\left(\frac{\pi}{L}x\right)}
\f]

from which:

\f[
    A_n =
    \begin{cases}
        A & \quad \textrm{for}\;n = 1\\[8pt]
        0 & \quad \textrm{for}\;n \ne 1
    \end{cases}
\f]

Hence:

\f[
    u(x,t) = A \sin{\left(\frac{\pi}{L}x\right)}\exp{\left(-D\frac{\pi^2}{L^2}t\right)}
\f]


\subsubsection constant Constant initial condition (test problem 3)


<img src="../../QA/test5.png" width="512">

If the initial condition is constant:

\f[
    \varphi(x,0) = U_0
\f]

then:

\f{align}
    A_n &= \dfrac{2U_0}{L} \int_0^L{\sin{\left(\dfrac{n\pi}{L}x\right)}dx} \nonumber\\[10pt]
        &= \dfrac{2U_0}{n\pi} \left(1 - \cos(n\pi)\right) \nonumber
\f}

Hence:

\f[
    A_n =
    \begin{cases}
        0                  & \quad \textrm{for}\;n = 0, 2, 4, ...\\[10pt]
        \dfrac{4U_0}{n\pi} & \quad \textrm{for}\;n = 1, 3, 5, ...
    \end{cases}
\f]

The solution is therefore:

\f[
    u(x,t) = \frac{4U_0}{\pi} \sum_n \frac{1}{2n-1}\sin\left(\frac{(2n-1)\pi}{L}x\right)\exp\left(-D\dfrac{(2n-1)^2\pi^2}{L^2}t\right)
\f]


\subsubsection electricblanket Chevron initial condition / electric blanket (test problem 4)


An alternative initial condition is:

\f[
    \varphi(x) =
    \begin{cases}
        T_0x     & \quad \textrm{for} \; 0   \le x \le L/2\\[8pt]
        T_0(L-x) & \quad \textrm{for} \; L/2 \le x \le L
    \end{cases}
\f]

where @f$ T_0 @f$ is a constant.

This can be thought of as representing an electric blanket of thickness @f$ L @f$ sandwiched between two insulating blankets, and whose surfaces at @f$ x = 0 @f$ and @f$ x = L @f$ are fixed at the ambient temperature, which we take to be @f$ u = 0 @f$ by choice of temperature scale. The initial value function then represents the steady-state temperature distribution through the thickness of the blanket. Then at @f$ t = 0 @f$ the blanket is turned off so that this temperature distribution forms the initial condition for the subsequent cooling phase.

The exact solution of this initial-value problem can be obtained using the same Fourier series method as above. First, we determine the Fourier series representation of the initial condition. We can look up the standard answer for a similar function:
\f[
    f(x) =
    \begin{cases}
        T_0x       & \quad \textrm{for} \; -\pi \le x \le 0 \\[8pt]
        T_0(\pi-x) & \quad \textrm{for} \; 0    \le x \le \pi
    \end{cases}
\f]

which is:

\f[
    f(x) = \frac{8A}{\pi^2} \left( \cos x + \frac{1}{9} \cos 3x + \frac{1}{25}\cos5x + ...\right)
\f]

where @f$ A @f$ is the amplitude and the period is @f$ 2\pi @f$. Shifting this by @f$ \pi/2 @f$ in the @f$ x @f$-direction gives:

\f[
    \begin{array}{lcl}
    f'(x) &=& \dfrac{8A}{\pi^2}
              \left(
                  \cos\left[x+\dfrac{\pi}{2}\right]
                  + \dfrac{1}{9} \cos 3\left[x+\dfrac{\pi}{2}\right]
                  + \dfrac{1}{25}\cos 5\left[x+\dfrac{\pi}{2}\right]
                  + ...
              \right)
    \\[8pt]
          &=& \dfrac{8A}{\pi^2}
              \left(
                  \sin x
                  - \dfrac{1}{9} \sin 3x
                  + \dfrac{1}{25}\sin 5x
                  - ...
              \right)
    \end{array}
\f]

which is equivalent to our starting condition with @f$ L = \pi @f$. Comparing this with the solution to the diffusion equation with @f$ t = 0 @f$ and @f$ L = \pi @f$:

\f[
    \varphi(x) = \sum_{n=1}^{\infty} A_n \sin\left(nx\right)
\f]

suggests that:

\f[
    A_n =
    \begin{cases}
        0                                                   & \quad \textrm{for} \; n = 2, 4, 6, ...\\[8pt]
        \left(-1\right)^{\frac{n-1}{2}}\dfrac{8A}{\pi^2n^2} & \quad \textrm{for} \; n = 1, 3, 5, ...
    \end{cases}
\f]

Hence the solution is:

\f[
    u(x,t) = \dfrac{4U_0}{\pi} \sum_{n=1}^{\infty} \left(-1\right)^{n-1} \dfrac{1}{(2n-1)^2} \sin\left((2n-1)x\right) \exp\left(D-(2n-1)^2D\right)
\f]


\subsection nonzeroboundaries Inhomogeneous boundary conditions


In the previous examples, the fact that @f$ u(0,t) = u(L,t) = 0 @f$ simplified the problem. We now address problems where this is not the case.

Let @f$ u(0,t) = u_0 @f$ and @f$ u(L,t) = u_L @f$.

The boundary conditions are not homogeneous, so we cannot apply separation of variables directly. However, we can transform the equation into an homogeneous one as follows.

Let:

\f[
    u(x,t) = v(x,t) + w(x)
\f]

so that the original equation:

\f[
    \dfrac{\partial u}{\partial t} = D \dfrac{\partial^2 u}{\partial x^2}
\f]

can be re-written:

\f[
    \dfrac{\partial v}{\partial t} = D \left( \dfrac{\partial^2 v}{\partial x^2} + \dfrac{\partial^2w}{\partial x^2}\right)
\f]

We can now, by requiring that:

\f[
    \dfrac{\partial^2w}{\partial x^2} = 0
\f]

with boundary conditions:

\f{align*}
    w(0) &= u(0,t) \\[8pt]
    w(L) &= u(L,t)
\f}

obtain a diffusion equation for @f$ v @f$:

\f[
    \dfrac{\partial v}{\partial t} = D \dfrac{\partial^2 v}{\partial x^2}
\f]

which, crucially, has homogeneous boundary conditions:

\f[
    \arraycolsep=1.4pt
    \begin{array}{llcl}
         v(0,t) &=& u(0,t) - w(0) &= 0 \\[8pt]
         v(L,t) &=& u(L,t) - w(L) &= 0
    \end{array}
\f]

Note that this imposes the restriction that the boundary conditions on @f$ u @f$ must be constant (say @f$ u_0 @f$ and @f$ u_L @f$, respectively).

Now @f$ v @f$ can be obtained as in [the previous section](\ref zeroboundaries). The initial condition is:

\f[
    v(x,0) = u(x,0) - w(x)
\f]

hence:

\f{align*}
    v(x,t) = \sum_{n=1}^{\infty} A_n \sin \left( \frac{n\pi}{L}x\right) \exp\left(-D\frac{n^2\pi^2}{L^2}t\right)
    \\[8pt]
    A_n = \frac{2}{L} \int_0^L \left(u(x,0) - w(x)\right) \sin \left( \frac{n\pi}{L}x\right) dx
\f}

Solving for @f$ w @f$, we obtain:

\f[
    w(x) = ax + b
\f]

and from the boundary conditions:

\f[
    \arraycolsep=1.4pt
    \begin{array}{lll}
        w(0) &= u(0,t) &= u_0\\[8pt]
        w(L) &= u(L,t) &= u_L
    \end{array}
\f]

we obtain:

\f{gather*}
    b = u_0 \\[8pt]
    a = \dfrac{u_L - u_0}{L} \\[8pt]
    w(x) = \dfrac{u_L - u_0}{L}x + u_0
\f}

Therefore the general solution is:

\f{align*}
    u(x,t) = \dfrac{u_L - u_0}{L}x + u_0 + \sum_{n=1}^{\infty} A_n \sin \left( \frac{n\pi}{L}x\right) \exp\left(-D\frac{n^2\pi^2}{L^2}t\right)
    \\[8pt]
    A_n = \frac{2}{L} \int_0^L \left(u(x,0) - \dfrac{u_L - u_0}{L}x + u_0\right) \sin \left( \frac{n\pi}{L}x\right) dx
\f}


\subsubsection zeroinit Zero initial condition


If @f$ u(x,0) = 0 @f$ then:

\f[
    w(x) = U_0\left(1 - \dfrac{x}{L}\right)
\f]

The solution is:

\f[
    u(x,t) = U_0 \left( 1 - \frac{x}{L} \right) - \frac{2U_0}{\pi} \sum_{n=1}^{\infty} \frac{1}{n} \sin\left(\frac{n\pi x}{L}\right) \exp\left( -\lambda_n^2 t \right)
\f]


\section laplacetransform Method: Laplace transforms


An alternative to using the separation of variables is the use of integral transforms, i.e. the Laplace and Fourier transforms. The idea is to eliminate one of the independent variables, transforming the original PDE into one containing derivatives with respect to smaller number of variables. For example, if the original PDE has just two independent variables, as does our one-dimensional diffusion equation, it is often possible to reduce the PDE to an ODE, which can then be solved. The solution can then be transformed back, to give the solution to the original PDE. There is no simple way to determine the choice of transform to use, or the choice of variable with respect to which the transform is to be taken.

It is well-known that a periodic function with period @f$ T @f$ can be represented over a fixed interval by a superposition of sinusoidal functions - i.e. as a Fourier series, which is written:

\f{align*}
    f(t) &= \dfrac{a_0}{2} + \sum_{n=1}^{\infty} { \left[ a_n \cos \left( \dfrac{2\pi nt}{T} \right) + b_n \left( \dfrac{2\pi nt}{T} \right) \right] } \\[8pt]
    a_n  &= \dfrac{2}{T} \int_{t_0}^{t_0+T} f(t) \cos\left( \dfrac{2\pi nt}{T} \right) dt \\[8pt]
    b_n  &= \dfrac{2}{T} \int_{t_0}^{t_0+T} f(t) \sin\left( \dfrac{2\pi nt}{T} \right) dt
\f}

or, since from Euler's equation:

\f[
    \exp\left(inx\right) = \cos nx + i\sin nx
\f]

in a more compact form:

\f{align*}
    f(t) &= \sum_{n=-\infty}^{\infty} c_n e^{i\omega_n t} \\[8pt]
    c_n  &= \frac{1}{T} \int_{t_0}^{t_0+T} f(t) e^{-i\omega_n t} dt
\f}

where @f$ \omega_n = 2\pi n/T@f$.

It is also possible, however, to represent functions that are defined over an infinite interval, and having no periodicity, in a similar way; this is called a Fourier transform, which is one of a class of representations called integral transforms. The Fourier transform may be considered a generalisation of the Fourier series representation of periodic functions to non-periodic functions. As the period @f$ T @f$ tends to infinity, the distance, in frequency space, between allowed frequencies, which is equal to @f$ \Delta\omega = 2\pi/T @f$, becomes vanishingly small, and the spectrum of allowed frequencies becomes continuous rather than quantised. The discrete coefficients of the Fourier series, @f$ c_n @f$, are replaced by a continuous function @f$ c(\omega) @f$.

The Fourier series coefficients are given by:

\f{align*}
    c_n  &= \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-i\omega_n t} dt \\[8pt]
         &= \frac{\Delta\omega}{2\pi} \int_{-T/2}^{T/2} f(t) e^{-i\omega_n t} dt
\f}

which, when substituted into the Fourier series, gives:

\f{align*}
    f(t) &= \frac{1}{2\pi} \sum_{n=-\infty}^{\infty} \Delta\omega \int_{-T/2}^{T/2} f(t') e^{-i\omega_n t'} dt' e^{i\omega_n t} \\[8pt]
         &= \frac{1}{2\pi} \sum_{n=-\infty}^{\infty} \Delta\omega \: g(\omega_n) e^{i\omega_n t}
\f}

and:

\f[
    g(\omega_n) = \int_{-T/2}^{T/2} f(t') e^{-i\omega_n t'} dt'
\f]

As @f$ L \rightarrow \infty @f$, and @f$ \Delta\omega @f$ becomes infinitesimal, the sum over discrete values becomes an integral:

\f[
    \sum_{n=-\infty}^{\infty} \Delta\omega \: g(\omega_n) e^{i\omega_n t} \rightarrow \int_{-\infty}^{\infty} g(\omega) e^{i\omega t} d\omega
\f]

Hence:

\f[
    f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(t') e^{-i\omega t'} dt' e^{i\omega t} d\omega
\f]

We call:

\f[
    \tilde f(\omega) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt
\f]

the Fourier transform of @f$ f(t) @f$, and:

\f[
    f(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \tilde f(\omega) e^{i\omega t} d\omega
\f]

Clearly the @f$ 1/\sqrt{2\pi} @f$ constant is arbitrary, the only requirement being that the product of the constants in the Fourier and inverse Fourier transforms should equal @f$ 1/2\pi @f$. This definition is chosen to be symmetric.

Next we consider the Laplace transform. The Fourier transform only exists for functions that tend to zero as @f$ t\rightarrow\infty @f$, so that the integral defining @f$ \tilde f @f$ converges. an example if @f$ f(t) = t @f$, which has no Fourier transform. Also, sometime we are only interested in a given function for @f$ t > 0 @f$, perhaps because the initial value @f$ f(0) @f$ is given in an initial-value problem. In these cases we turn to the Laplace transform, @f$ \tilde f(s) = \mathcal{L}\left[f(t)\right] @f$:

\f[
    \tilde f(s) = \int_0^\infty f(t) e^{-st} dt
\f]

This converts functions of @f$ t @f$ to functions of a new variable @f$ s @f$. The transformation is linear, i.e.:

\f[
    \mathcal{L} \left[ c_1 f_1(t) + c_2 f_2(t) \right] = c_1 \mathcal{L}\left[ f_1(t) \right] + c_2 \mathcal{L}\left[f_2(t) \right]
\f]

Unlike with Fourier transforms, the inverse Laplace transform is not straightforward, and often performed using a look-up table of common functions together with their Laplace transforms.

The Laplace transform of a derivative is:

\f{align*}
    \mathcal{L}\left[\frac{df}{dt}\right] &= \int_0^\infty \frac{df}{dt} e^{-st} dt \\[8pt]
                                          &= \left[ f(t) e^{-st} \right]_0^\infty + s \int_0^\infty f(t) e^{-st} dt \\[8pt]
                                          &= -f(0) + s\tilde f(s)
\f}

Hence:

\f[
    \tilde{f'} = s\tilde f - f(0)
\f]

Higher-order derivatives are easily found, e.g.:

\f{align*}
    \tilde{f''} &= s\tilde{f'} - f'(0) \\[8pt]
                &= s^2\tilde f - sf(0) - f'(0)
\f}

and:

\f{align*}
    \tilde{f'''} &= s\tilde{f''} - f''(0) \\[8pt]
                 &= s^3\tilde f - s^2f(0) - sf'(0) - f''(0)
\f}

Generalising from these examples gives:
\f[
    \begin{array}{lcl}
    \tilde{f^{(n)}} &=& s^n\tilde{f(s)} - s^{n-1}f(0) - s^{n-2} f^{(1)}(0) - ... - sf^{(n-2)}(0) - f^{(n-1)}(0)
    \end{array}
\f]
where the superscripts in parentheses denote derivatives.

Using this formula, we can often remove the derivatives from an ODE (linear with constant coefficients) by taking its Laplace transform, resulting in an algebraic equations for the Laplace transform of the desired solution, which when solved can be transformed back to obtain the solution.

In PDEs, as mentioned, Laplace tranformation can remove one of the independent variables, reducing a PDE to an ODE in the particular case where there are two independent variables.


\section infdomain Infinite domain solutions


We now consider solutions of the diffusion equation for infinite or semi-infinite domains.


\subsection nonzerobcon Semi-infinite: non-zero boundary condition


\subsubsection zeroinitcon Zero initial condition


Consider a semi-infinite slab with constant diffusion coefficient, governed by:

\f[
    \frac{\partial u}{\partial t} = D\frac{\partial^2 u}{\partial x^2}
\f]

having initial condition:

\f[
    u(x,0) = 0
\f]

and boundary condition:

\f[
    u(0,t) = U_0
\f]

We choose the Laplace transform since we are interested in @f$ t > 0 @f$, and take the Laplace transform with respect to @f$ t @f$:

\f{gather*}
    \int_0^\infty \frac{\partial u}{\partial t} e^{-st} dt = \int_0^\infty D\frac{\partial^2 u}{\partial x^2}  e^{-st} dt \\
    s \tilde u(x,s) - u(x,0)                               = D\frac{\partial^2}{\partial x^2} \int_0^\infty u e^{-st} dt \\
    s \tilde u(x,s)                                        = D\frac{\partial^2 \tilde u}{\partial x^2}
\f}

the solution to which is:

\f[
    \tilde u(x,s) = A(s) \exp\left(\sqrt{\frac{s}{D}}x\right) + B(s) \exp\left(-\sqrt{\frac{s}{D}}x\right)
\f]

We require that @f$ u(x,t) \rightarrow 0 @f$ as @f$ t \rightarrow \infty @f$, so @f$ \tilde u(x,s) \rightarrow 0 @f$ as @f$ t \rightarrow \infty @f$; therefore we require @f$ A = 0 @f$. As a result, @f$ B = \tilde u(0,s) @f$. Since @f$ u(0,t) = U_0 @f$:

\f[
    B(s) = \tilde u(0,s) = \mathcal{L}\left[ u(0,t) \right] = \int_0^\infty U_0 e^{-st} dt = \frac{U_0}{s}
\f]

Hence:

\f[
    \tilde u(x,s) = \frac{U_0}{s} \exp\left(-\sqrt{\frac{s}{D}}x\right)
\f]

The inversion of this is difficult, so we only give the result:

\f[
    u(x,t) = U_0\left[ 1 - \mathrm{erf}\left( \frac{x}{\sqrt{4Dt}} \right) \right]
\f]


\subsection infinite Infinite


An infinite geometry has no boundary conditions, so only the initial condition can be specified. For an arbitrary initial distribution, @f$ \varphi(x) @f$, the distribution at a later time can be determined at a later time @f$ t @f$.

Since we are interested in values of @f$x@f$ from @f$ -\infty @f$ to @f$ \infty @f$, this suggests Fourier transformation with respect to the @f$ x @f$-variable.

\f[
      \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \frac{\partial u}{\partial t}      e^{-i\omega x} dx
    = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} D\frac{\partial^2 u}{\partial x^2} e^{-i\omega x} dx
\f]

Hence:

\f{gather*}
      \frac{1}{\sqrt{2\pi}} \frac{\partial}{\partial t} \int_{-\infty}^{\infty} u e^{-i\omega x} dx
    = \frac{D}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \frac{\partial^2 u}{\partial x^2} e^{-i\omega x} dx \\[8pt]
      \frac{\partial \tilde u}{\partial t}
    = \frac{D}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \frac{\partial^2 u}{\partial x^2} e^{-i\omega x} dx
\f}

The derivative of a Fourier transform is related to the derivative of the function being transformed via:

\f[
    \mathcal{F}\left[f'(x)\right] = i\omega \mathcal{F}\left[f(t)\right]
\f]

Therefore:

\f[
    \begin{array}{lcl}
    \frac{\partial \tilde u(\omega,t)}{\partial t} &=& -D\omega^2 \tilde u(\omega,t)
    \end{array}
\f]

The solution of this equation is:

\f[
    \tilde u(\omega,t) = \tilde u(\omega,0) e^{-D\omega^2 t}
\f]

The initial condition is:

\f{align*}
    \tilde u(\omega,0) &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} u(x,0) e^{-i\omega x} dx \\[8pt]
                       &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \varphi(x) e^{-i\omega x} dx \\[8pt]
                       &= \tilde \varphi(\omega)
\f}

Hence the solution becomes:

\f{align*}
    \tilde u(\omega,t) &= \tilde \varphi(\omega) e^{-D\omega^2 t} \\[8pt]
                       &= \sqrt{2\pi} \tilde \varphi(\omega) \tilde G(\omega t)
\f}

where we have defined:

\f[
    \tilde G(\omega t) = \frac{1}{\sqrt{2\pi}}e^{-D\omega^2 t}
\f]

We can now use the convolution theorem, since @f$ \tilde u @f$ can be expressed as the product of two Fourier transforms. The convolution theorem states that, if we have a convolution:

\f[
    h(z) = \int_{-\infty}^{\infty} f(x) g(z-x) dx
\f]

then:

\f[
    \tilde h(\omega) = \sqrt{2\pi} \tilde f(\omega)\tilde g(\omega)
\f]

Hence:

\f[
    u(x,t) = \int_{-\infty}^{\infty} \varphi(x') G(x-x',t) dx
\f]

where @f$ G(x,t) @f$ is the Green's function for this problem. This is the inverse Fourier transform of @f$ \tilde G(\omega,t) @f$:

\f{align*}
    G(x,t) &= \frac{1}{\sqrt{2\pi}}               \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}}e^{-D\omega^2 t} e^{i\omega x} d\omega \\[8pt]
           &= \frac{1}{2\pi}                      \int_{-\infty}^{\infty}                      e^{-D\omega^2 t} e^{i\omega x} d\omega \\[8pt]
           &= \frac{1}{2\pi} e^{\frac{-x^2}{4Dt}} \int_{-\infty}^{\infty}                      e^{-Dt\left(\omega + \frac{ix}{2Dt}\right)^2}  d\omega \\[8pt]
           &= \frac{1}{2\pi} e^{\frac{-x^2}{4Dt}} \int_{-\infty}^{\infty}                      e^{-Dt\omega'}  d\omega' \\[8pt]
           &= \frac{1}{\sqrt{4\pi Dt}} e^{\frac{-x^2}{4Dt}}
\f}

where @f$ k' = k - ix/2Dt @f$ and in the final step we have used the standard result for the integral of a Gaussian. Thus, and finally, we have:

\f[
    u(x,t) = \frac{1}{\sqrt{4\pi Dt}} \int_{-\infty}^{\infty} \exp\left[-\frac{(x-x')^2}{4Dt}\right] \varphi(x') dx
\f]


\subsubsection deltafunc Delta function initial condition


If the initial condition is a delta function @f$ \varphi(x) = \delta(x-a) @f$ (i.e. a point source at @f$ x = a @f$) then the distribution at time @f$ t @f$ is simply:

\f[
    u(x,t) = G(x-a,t) = \frac{1}{\sqrt{4\pi Dt}}  \exp\left[-\frac{(x-a)^2}{4Dt}\right]
\f]

http://excelcalculations.blogspot.co.uk/2011/04/solving-1d-heat-equation-using-finite.html
