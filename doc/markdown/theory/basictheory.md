Basic Theory    {#basictheorypage}
============

\tableofcontents


\section diffusionequation Diffusion Equation


\subsection Introduction


The diffusion equation is a partial differential equation that governs the density distribution of a substance or material undergoing diffusion:

\f[
  \dfrac{\partial u}{\partial t}
  = \nabla \cdot \left( D\left(\mathbf{r}, t\right) \nabla u\left(\mathbf{r}, t\right) \right) + Q\left(\mathbf{r}, t\right)
  \label{DiffusionEquation}
\f]

where:

- @f$ \mathbf{r} = (x,y,z) @f$ is position
- @f$ t @f$ is time
- @f$ u \left( \mathbf{r}, t \right) @f$ is the unknown, i.e. density or concentration of the diffusing quantity
- @f$ D \left( \mathbf{r}, t \right) @f$ is the _diffusion coefficient_
- @f$ Q \left( \mathbf{r}, t \right) @f$ is the source density

In general, the diffusion coefficient can depend also on the local density @f$ D\left( u\left( \mathbf{r},t \right), \mathbf{r}, t\right) @f$, yielding a non-linear diffusion equation. However, we will only consider the linear version here. Note also, the inhomogeneous diffusion equation, where @f$ Q @f$ is non-zero, is considered for completeness; but often practical problems do not include a source term, and the simpler homogeneous version is enough.

From hereon we will display the quantities @f$ D @f$, @f$ Q @f$ and @f$ u @f$ without their arguments, for simplicity of notation.


\subsection Derivation


To derive the diffusion equation we begin with Fick's law @ref ref01 "(Fick, 1855)":

\f[
  \mathbf{F} = -D \nabla u
\f]

The vector field @f$ \mathbf{F} @f$ is the flux, which is the rate of transfer per unit area; the integral of the normal component of @f$ \mathbf{F} @f$ over a given surface is equal to the rate of flow through the surface. The direction of the flux vector is normal to the surface of constant concentration. Fick's law says that for a given concentration @f$ u @f$ at a given point @f$ \mathbf{r} @f$, the flux is proportional to the concentration gradient there, and has the opposite direction.

The diffusion equation arises by combining Fick's Law with the _continuity equation_, which describes the conservation law for the diffusing substance. That is, by conservation:

\f[
  \dfrac{\partial u}{\partial t} = - \nabla \cdot \mathbf{F} + Q
\f]

The divergence of the flux @f$ \mathbf{F} @f$, i.e. @f$ \nabla \cdot \mathbf{F} @f$, is the rate of loss of concentration per unit time from the volume element. As above, @f$ Q @f$ is the source density: the concentration produced per unit time per unit volume.

By substituting Fick's Law:

\f[
  \dfrac{\partial u}{\partial t} = \nabla \cdot D \nabla u + Q
\f]

As we saw above, this is the diffusion equation (sometimes known as Fick's second law).


\subsection specialcases Special Cases


In the special case that @f$ D @f$ is constant in space, then this equation simplifies to:

\f[
  \dfrac{\partial u}{\partial t} = D \nabla^2 u + Q
\f]

and in steady-state, @f$ \dfrac{\partial u}{\partial t} = 0 @f$, and with constant source, it reduces to Poisson's equation:

\f[
  \nabla^2 u = \dfrac{Q}{D}
\f]

and further to Laplace's equation if the source term is zero:

\f[
  \nabla^2 u = 0
\f]


\subsection geometry Geometry

> **Implementation note:** The current solver implementation supports only planar
> (slab) geometry. Cylindrical and spherical geometries are documented here for
> theory completeness but are not yet implemented in the code.


Returning now to the full equation, we recall that:

\f{align*}
    \nabla &= \hat i \dfrac{\partial}{\partial x} + \hat j \dfrac{\partial}{\partial y} + \hat k \dfrac{\partial}{\partial z} \\[8pt]
           &= \hat e_{\rho} \dfrac{\partial}{\partial \rho} + \hat e_{\phi} \dfrac{\partial}{\partial \phi} + \hat e_z \dfrac{\partial}{\partial z} \\[8pt]
           &= \hat e_{r} \dfrac{\partial}{\partial r} + \hat e_{\theta} \dfrac{\partial}{\partial \theta} + \hat e_{\phi} \dfrac{\partial}{\partial \phi}
\f}

in Cartesian, cylindrical and spherical geometries, respectively.

Consider first spherical geometry:

\f[
  \nabla \cdot D \nabla u =
  \frac{1}{r^2}           \frac{\partial}{\partial r}      \left( r^2 D                    \frac{\partial u}{\partial r}      \right) +
  \frac{1}{r \sin \theta} \frac{\partial}{\partial \theta} \left( \frac{D \sin \theta }{r} \frac{\partial u}{\partial \theta} \right) +
  \frac{1}{r \sin \theta} \frac{\partial}{\partial \phi}   \left( \frac{D}{r \sin \theta}  \frac{\partial u}{\partial \phi}   \right)
\f]

In cylindrical geometry:

\f[
  \nabla \cdot D \nabla u =
  \frac{1}{\rho} \frac{\partial}{\partial \rho} \left( \rho D         \frac{\partial u}{\partial \rho} \right) +
  \frac{1}{\rho} \frac{\partial}{\partial \phi} \left( \frac{D}{\rho} \frac{\partial u}{\partial \phi} \right) +
                 \frac{\partial}{\partial z}    \left( D              \frac{\partial u}{\partial z}    \right)
\f]

and in Cartesian geometry:

\f[
  \nabla \cdot D \nabla u =
  \frac{\partial}{\partial x}\left( D \frac{\partial u}{\partial x} \right) +
  \frac{\partial}{\partial y}\left( D \frac{\partial u}{\partial y} \right) +
  \frac{\partial}{\partial z}\left( D \frac{\partial u}{\partial z} \right)
\f]

In one dimension:

\f{align*}
  \dfrac{\partial u}{\partial t} &= \dfrac{1}{r^2}  \dfrac{\partial}{\partial r}    \left( r^2  D \dfrac{\partial u}{\partial r}    \right) + Q \\[8pt]
  \dfrac{\partial u}{\partial t} &= \dfrac{1}{\rho} \dfrac{\partial}{\partial \rho} \left( \rho D \dfrac{\partial u}{\partial \rho} \right) + Q \\[8pt]
  \dfrac{\partial u}{\partial t} &=                 \dfrac{\partial}{\partial x}    \left(      D \dfrac{\partial u}{\partial x}    \right) + Q
\f}

These equations can be generalised:

\f[
  \frac{\partial u}{\partial t} = \frac{1}{x^p} \frac{\partial}{\partial x} \left(x^p D \frac{\partial u}{\partial x} \right) + Q
\f]

where:

- @f$ p = 0 @f$ for plane geometry
- @f$ p = 1 @f$ for 1D cylindrical geometry, and
- @f$ p = 2 @f$ for 1D spherical geometry.


\subsection heatflowequation Heat Flow Equation


The phenomena of heat conduction and diffusion are basically the same, and Fick @ref ref01 "(Fick, 1855)" first put diffusion on a quantitative basis by adopting the mathematical equation of heat conduction derived by Fourier @ref ref02 "(Fourier, 1822)".

The heat flow equation of Fourier is:

\f[
  a \frac{\partial \theta}{\partial t} = \frac{\partial}{\partial x} K \frac{\partial \theta}{\partial x}
\f]

where @f$ a @f$ is the heat capacity of the material per unit volume and @f$ K @f$ is the thermal conductivity. For constant conductivity this becomes:

\f[
  \frac{\partial \theta}{\partial t} = \frac{K}{a} \frac{\partial^2 \theta}{\partial x^2}
\f]

where the corresponding equation for diffusion is:

\f[
  \frac{\partial u}{\partial t} = D \frac{\partial^2 u}{\partial x^2}
\f]

For the two equations to correspond, we equate temperature @f$ \theta @f$ with concentration @f$ u @f$, which clearly implies that @f$ D = K/a @f$. However, it is also the case that:

\f[
  \mathbf{F} = -K \nabla \theta
\f]

which, when compared with Fick's law for diffusion

\f[
  \mathbf{F} = -D \nabla u
\f]

implies that @f$ D = K @f$, and therefore that in diffusion, unlike in heat conduction, @f$ a = 1 @f$. This is because we have identified @f$ u @f$ with @f$ \theta @f$ (temperature), whereas in heat conduction, the diffusing 'substance' is heat, not temperature. The factor @f$ a @f$ is needed to convert temperature to the amount of heat per unit volume, whereas in diffusion, the concentration is already by definition the amount of substance per unit volume, so @f$ a = 1 @f$.
