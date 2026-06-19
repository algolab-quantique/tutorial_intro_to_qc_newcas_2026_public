# NEWCAS 2026 Tutorial: Introduction to Quantum Computing
Led by *Joshua T. Cantin*

Material adapted from that by *Jean-Frédéric Leprade*, *Tania Belabbas*, *Ibrahim Chegrane*, and *Isabelle Viarouge*

Here, you will find the notebooks needed for this tutorial.

The folder [1_qiskit_intro](1_qiskit_intro) contains an introduction to quantum gates and using Qiskit.

The folder [2_qiskit_excecution](2_qiskit_excecution) contains an introduction to running quantum circuits on the simulators provided by Qiskit.

The folder [3_time_evolution](3_time_evolution) contains the Trotterisation of a small physics simulation (transverse field Ising model).

The folder [4_grover](4_grover) contains an example of the Grover algorithm, as applied to a toy SAT problem.

# Running Instructions

To run the notebooks contained in the folders, do the following:

1. Follow the coding environment setup as given in [SETUP.md](SETUP.md) if not already completed. You don't have to use it, but it is a good fall back if something is not working.
1. Then, using the operating system terminal (not the terminal inside VS Code), install Python 3.12 with `pyenv install 3.12`.
1. Activate the python version with `pyenv shell 3.12`
1. Create a clean Python environment with `python -m venv env_qc_newcas`
1. Activate the environment: `source env_qc_newcas/bin/activate`
1. Upgrade pip: `python -m pip install --upgrade --require-hashes --no-deps -r toolchain.txt`
    
    This and the next step are needed to help avoid recent supply chain attacks that have targeted packages as fundamental as numpy.
1. Install needed packages securely: `python -m pip install --require-hashes -r requirements.txt`
    
    It is possible that the above command will not work on some Windows machines when not using WSL2. If so, you can try the following:
    1. `python -m pip install --require-hashes --no-deps -r requirements.txt`
    1. Then, if you get a missing dependency error when running the notebook, you can run `python -m pip install [package_name]` with `[package_name]` replaced by the needed dependency. 
    
        This workaround, while previously normal for more than a decade now, is less secure. So, if you prefer using WSL2 to avoid this, there are installation instructions in SETUP.md.
    
    While the packages install, read ahead in the notebook.
1. Open the notebook in VS Code
1. Select the kernel 
    1. Click on the `Select Kernel` button at the top-right of the notebook
    1. Choose Python environment
    1. Select `env_qc_newcas`