"""Reproduce the numerical figures for the Abel--Liouville pedagogical paper.

Uses NumPy, SciPy and Matplotlib. All files are written beside this script.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.linalg import expm

OUT = Path(__file__).resolve().parent

def plot_volume_factors():
    t = np.linspace(0, 3, 501)
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    for c in [1, 0, -1]:
        ax.plot(t, np.exp(c*t), label=rf'$\operatorname{{tr}} A={c}$')
    ax.set(xlabel='$t$', ylabel='$V(t)/V(0)$', title='Volume evolution from Liouville\'s formula')
    ax.grid(alpha=.3);ax.legend();fig.tight_layout()
    fig.savefig(OUT/'figures_volume_factors.png', dpi=300)
    plt.close(fig)

def plot_oscillator_phase_space():
    t=np.linspace(0,30,3001)
    fig,ax=plt.subplots(figsize=(6,5))
    for g in [0.,.12]:
        def rhs(t,y): return [y[1],-y[0]-2*g*y[1]]
        sol=solve_ivp(rhs,(0,30),[1,0],t_eval=t,rtol=1e-11,atol=1e-13)
        ax.plot(sol.y[0],sol.y[1],label=rf'$\gamma={g:g}$')
    ax.set(xlabel='$x$',ylabel="$v=\\mathrm{d}x/\\mathrm{d}t$",title='Damped oscillator in phase space')
    ax.grid(alpha=.3);ax.legend();fig.tight_layout()
    fig.savefig(OUT/'figures_oscillator_phase_space.png',dpi=300)
    plt.close(fig)

def polygon_area(coords):
    x,y=coords[0],coords[1]
    return .5*abs(np.dot(x,np.roll(y,-1))-np.dot(y,np.roll(x,-1)))

def plot_oscillator_area():
    """Check expm against Liouville's area law with a fixed 720-gon.

    The shoelace-area ratio of a polygon under a linear map is exactly
    abs(det(map)); no circle-versus-polygon discretization error survives
    this ratio. Residual differences reflect expm and floating-point error.
    """
    gamma=.12
    A=np.array([[0.,1.],[-1.,-2*gamma]])
    theta=np.linspace(0,2*np.pi,720,endpoint=False)
    circle=np.vstack((np.cos(theta),np.sin(theta)))
    unit_area=polygon_area(circle)
    t_sample=np.linspace(0,10,16)
    ratios=[]
    for t in t_sample:
        ell=expm(t*A)@circle
        ratios.append(polygon_area(ell)/unit_area)
    predicted=np.exp(-2*gamma*t_sample)
    assert np.max(abs(np.array(ratios)-predicted))<5e-13
    fig,(ax0,ax1)=plt.subplots(1,2,figsize=(10.5,4.1))
    for t in [0.,4.,8.]:
        ell=expm(t*A)@circle
        ax0.plot(np.r_[ell[0],ell[0,0]],np.r_[ell[1],ell[1,0]],label=f'$t={t:g}$, $A/A_0={np.exp(-.24*t):.3f}$')
    ax0.set(xlabel='$x$',ylabel='$v$',title='(a) Transported unit disk')
    ax0.set_aspect('equal',adjustable='box');ax0.grid(alpha=.25);ax0.legend(fontsize=8)
    t=np.linspace(0,10,500)
    ax1.plot(t,np.exp(-2*gamma*t),label='Liouville $e^{-0.24t}$')
    ax1.plot(t_sample,ratios,'o',markersize=3.3,label='720-gon area ratio (expm)')
    ax1.set(xlabel='$t$',ylabel='$V(t)/V(0)$',title='(b) Consistency of expm and Liouville law')
    ax1.grid(alpha=.25);ax1.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT/'figures_oscillator_area.png',dpi=300)
    plt.close(fig)

if __name__=='__main__':
    plot_volume_factors()
    plot_oscillator_phase_space()
    plot_oscillator_area()
