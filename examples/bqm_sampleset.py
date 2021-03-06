import dimod
import dwave.inspector
from dwave.system import DWaveSampler, EmbeddingComposite


# define problem
bqm = dimod.BQM.from_ising({}, {'ab': 1, 'bc': 1, 'ca': 1})

# get sampler
print("sampler init")
sampler = EmbeddingComposite(DWaveSampler())

# sample
print("sampling")
sampleset = sampler.sample(bqm, num_reads=100, chain_strength=1,
                           label='bqm/sampleset inspector example')

# inspect
print("inspecting")
dwave.inspector.show(bqm, sampleset)
