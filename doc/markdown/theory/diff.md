Differencing {#differencing}
============


\tableofcontents


\section explicitscheme Explicit Scheme


Now consider differencing.

Beginning with the 1D Cartesian diffusion equation with no source terms and constant diffusion coefficient, we have the following simplest explicit differencing scheme, where we have taken a forward difference in time and a central difference in space. It is commonly known as the FTCS (forward-in-time, centred-in-space) scheme:

\f[
    \frac{u^{n+1}_j - u^n_j}{\Delta t} =
    D \frac{u^n_{j+1} - 2 u^n_j + u^n_{j-1}}{\Delta x^2}
\f]

where @f$ n @f$ is the time index and @f$ j @f$ the spatial index, and @f$ \Delta x @f$ and @f$ \Delta t @f$ the mesh size and time-step, respectively.

Hence:
\f[
    u^{n+1}_j =
    \alpha \left( u^n_{j+1} - 2 u^n_j + u^n_{j-1} \right) + u^n_j
\f]
where @f$ \alpha = D \Delta t / \Delta x^2 @f$.  The scheme is referred to as explicit because the value of @f$ u_j @f$ at time level @f$ n + 1 @f$, which we intend to calculate, is dependent on quantities only at time level @f$ n @f$, which are known. Later, we will consider implicit methods for which the value of @f$ u_j @f$ at time level @f$ n + 1 @f$ is dependent on neighbouring quantities at time level @f$ n + 1 @f$, and therefore which must be solved simultaneously for all @f$ j @f$.

From hereon we will use the symbol @f$ \delta^2 @f$ to represent the central difference in space, i.e.:
\f[
    u^{n+1}_j =
    \alpha \left( \delta^2 u \right)^n_j + u^n_j
\f]


\subsection explicitstability Stability analysis


To analyse the stability of a given discretisation, assume that:
\f[
    U_j^n = u_j^n + \epsilon
\f]
where @f$ u @f$ is the exact solution of the discretised equations, @f$ U @f$ is the solution computed in the presence of floating-point round-off error, and @f$ \eta @f$ is the error. If we assume the @f$ U @f$ satisfies the discretised equation, then @f$ \epsilon @f$ does too:

\f[
    \epsilon^{n+1}_j =
    \alpha \left( \delta^2 \epsilon \right)^n_j + \epsilon^n_j
\f]

We can expand @f$ \epsilon @f$ in a Fourier series with respect to @f$ x @f$, over the interval @f$ L @f$:

\f[
    \epsilon(x,t) = \sum_{n=-N}^N E_n(t) e^{ik_nx}
\f]

where @f$ k_n = \dfrac{n\pi}{L} @f$ and @f$ N = \dfrac{L}{\Delta x} @f$. We only need to consider the growth of the error in a single Fourier mode @f$ n = m @f$:

\f[
    \epsilon_m(x,t) = E_m(t)e^{ik_mx}
\f]

Substituting this into the error equation:

\f[
    E_m(t+\Delta t) =
    \alpha \left[ E_m(t)e^{ik_m\Delta x} - 2 E_m(t) + E_m(t)e^{-ik_m\Delta x} \right] + E_m(t)
\f]
\f[
    g =
    \dfrac{E_m(t+\Delta t)}{E_m(t)} =
    \alpha \left( e^{ik_m\Delta x} - 2 + e^{-ik_m\Delta x} \right) + 1
\f]

where we have defined @f$ g @f$, the growth or _amplification factor_, to be the factor by which the error amplitude grows each time-step. Using the identity:

\f[
    \sin{\theta} = \dfrac{e^{i\theta} - e^{-i\theta}}{2i}
    \sin^2{\theta} = \dfrac{e^{2i\theta} + e^{-2i\theta} - 2}{-4}
\f]

we have:

\f[
    -4\sin^2{\dfrac{k_m\Delta x}{2}} = \left( e^{ik_m\Delta x} - 2 + e^{-ik_m\Delta x} \right)
\f]

Hence:

\f[
    g = 1 - 4\alpha \sin^2{\dfrac{k_m\Delta x}{2}}
\f]

Since the condition for stability is that @f$ g \le 1 @f$, we have therefore:

\f[
    \alpha \sin^2{\dfrac{k_m\Delta x}{2}} \le \dfrac{1}{2}
\f]

We want this to hold for all values of @f$ k_m @f$, but the @f$ \sin^2 @f$ term cannot exceed @f$ 1 @f$, hence:

\f[
    \alpha = \dfrac{D\Delta t}{\Delta x^2} \le \dfrac{1}{2}
\f]
\f[
    \Delta t \le \dfrac{\Delta x^2}{2D}
\f]

The scheme is conditionally stable, but requires a factor of four more time-steps for every doubling of the mesh resolution; hence to double the resolution would increase cost by a factor of eight.


\section implicitdifferencing Implicit Differencing


The discretisation above employs a forward time difference. Using instead a backward time difference gives:

\f[
  \frac{u^{n+1}_j - u^n_j}{\Delta t} =
  D \frac{u^{n+1}_{j+1} - 2 u^{n+1}_j + u^{n+1}_{j-1}}{\Delta x^2}
\f]

or:

\f[
  u^{n+1}_j =
  \alpha \left( \delta^2 u \right)^{n+1}_j + u^n_j
\f]

which is exactly the same as the explicit scheme except for the superscripts on the right-hand side. In this scheme, one must solve a set of simultaneous equations to obtain the @f$ u_j^{n+1} @f$. Unlike the explicit scheme, this equation is stable under all conditions.

The forward and backward time differencing schemes can be combined into a general system in which the right-hand side is a weighted average of the right-hand sides of the simple explicit and implicit schemes:
\f[
  \frac{u^{n+1}_j - u^n_j}{\Delta t} =
  \theta       D \frac{u^{n+1}_{j+1} - 2 u^{n+1}_j + u^{n+1}_{j-1}}{\Delta x^2} +
  (1 - \theta) D \frac{u^{n}_{j+1}   - 2 u^{n}_j   + u^{n}_{j-1}}{\Delta x^2}
\f]
or:
\f[
  u^{n+1}_j = \alpha
  \left[ \theta \left(\delta^2 u \right)^{n+1}_j +
  (1 - \theta)  \left(\delta^2 u \right)^{n}_j
  \right] + u^n_j
\f]
where @f$ \theta @f$ is a constant, @f$ 0 \le \theta \le 1 @f$. If @f$ \theta = 0 @f$ the explicit scheme above is retrieved. If @f$ \theta = 1/2 @f$, the well-known Crank-Nicholson scheme is obtained.

For @f$ 1/2 \le \theta \le 1 @f$ the difference system is unconditionally stable, whereas for @f$ 0 \le \theta < 1/2 @f$ the time-step must be restricted according to:
\f[
  \frac{2D\Delta t}{\Delta x^2} \le \frac{1}{1 - 2\theta}
\f]
to remain stable.


\section variablecoefficients Variable Coefficients


The more general case where @f$ D = D(x) @f$, rather than being constant, leads to the diffusion equation in 1D being written:

\f[
  \frac{\partial u}{\partial t} = \frac{\partial}{\partial x} D \frac{\partial u}{\partial x}
\f]

The difference equation generalises to:

\f[
  \frac{u_j^{n+1} - u_j^{n}}{\Delta t} =
  \frac{\theta\left[\delta(D\delta u)\right]_j^{n+1} + (1-\theta)\left[\delta(D\delta u)\right]_j^{n}}
       {\Delta x^2}
\f]

or:

\f[
  u_j^{n+1} =
  \theta\left[\delta(\alpha\delta u)\right]_j^{n+1} + (1-\theta)\left[\delta(\alpha\delta u)\right]_j^{n}
   + u_j^{n}
\f]

where now @f$ \alpha = \alpha(x) = D(x) \Delta t/\Delta x^2 @f$. The equations to be solved are:

\f[
  \left( -\theta\alpha_{j+1/2} \right)                          u_{j+1}^{n+1} +
  \left( 1 + \theta\alpha_{j+1/2} + \theta\alpha_{j-1/2} \right)u_{j}^{n+1}   +
  \left( -\theta\alpha_{j-1/2} \right)                          u_{j-1}^{n+1} =
  b_j
\f]

or:

\f[
  -A_j u_{j+1}^{n+1} +
  B_j  u_{j}^{n+1}   -
  C_j  u_{j-1}^{n+1} =
  b_j
\f]

where:

\f[
  \def\arraystretch{2}
  \begin{array}{lcl}
  A_j &=& \theta\alpha_{j+1/2}                            \\
  B_j &=& 1 + \theta\alpha_{j+1/2} + \theta\alpha_{j-1/2} \\
  C_j &=& \theta\alpha_{j-1/2}
  \end{array}
\f]

and @f$ b_j @f$ contains all the known quantities.


\section solutionmethod Solution Method


The set of linear equations:

\f[
  -A_j u_{j+1} +
  B_j  u_{j}   -
  C_j  u_{j-1} =
  b_j
\f]

forms a tri-diagonal matrix, for which the standard matrix inversion methods are inefficient. Given a fixed boundary condition at @f$ j = 0 @f$, any value of @f$ u_j @f$ at @f$ j = 1 @f$ determines the whole solution. We can write:

\f[
  u_j = E_j u_{j+1} + F_j
\f]

Substituting @f$ E_{j-1} u_j + F_{j-1} @f$ for @f$ u_j @f$ into the difference equation gives:

\f[
  -A_j u_{j+1} +
  B_j  u_{j}   -
  C_j  \left( E_{j-1} u_j + F_{j-1} \right) =
  b_j
\f]

Hence:

\f[
  u_j = \frac{A_j}{B_j - C_j E_{j-1}} u_{j+1} + \frac{b_j + C_j F_{j-1}}{B_j - C_j E_{j-1}}
\f]

and therefore:

\f[
  \def\arraystretch{2.8}
  \begin{array}{lcl}
  E_j &=& \dfrac{A_j}{B_j - C_j E_{j-1}} \\
  F_j &=& \dfrac{b_j + C_j F_{j-1}}{B_j - C_j E_{j-1}}
  \end{array}
\f]

These equations can be solved recursively to find the @f$ E_j @f$ and @f$ F_j @f$ in order of increasing @f$ j @f$, with @f$ E_0 @f$ and @f$ F_0 @f$ being determined from the left-hand boundary condition. Then the @f$ u_j @f$ can be calculated in order of decreasing @f$ j @f$ from the right-hand boundary condition.

Clearly if the left-hand boundary condition is @f$ u_0 = 0 @f$, then @f$ E_0 = 0 @f$, @f$ F_0 = 0 @f$. If @f$ u_0 \ne 0 @f$ but some non-zero constant, then @f$ E_0 = 0 @f$ and @f$ F_0 = u_0 @f$.
