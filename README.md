---
author: "Hien Trinh"
---
# NGS-SELEX pipeline for sequence preferences of nucleosome positioning sequences

## Summary
 
Nucleosomes are the fundamental organizing unit of all eukaryotic genomes. Each nucleosome is composed of an octameric complex of the core histone proteins around which ~147 bp of DNA is wrapped. Although the sequences of histone proteins are highly conserved, they still show significant amino acid sequence variations. In previous work in our laboratory, histone protein sequences from eight eukaryotic organisms representing the diversity of genomic properties expressed as recombinant proteins were tested <em>in vitro</em> for the assembly of tetramers, octamers and nucleosome formation. Compared to human histones assembled into nucleosomes with an artificial positioning DNA, those assembled from <em>Plasmodium falciparum</em> histones were observed to be somewhat more stable and less dynamic, while those from <em>Encephalitozoon cuniculi</em> were less stable and more dynamic. The histone octamers of these three organisms were used for systematic evolution of ligands by exponential enrichment (SELEX) with a human mononucleosomal DNA library to study the sequence preferences of each organism octamer. In this bioinformatic analysis, a pipeline has been developed for processing the resulting next generation sequencing (NGS) reads from different rounds of SELEX for each octamer. This has allowed the full length selected DNA fragments to be regenerated by mapping to the human genome. The trajectory of selection in the SELEX has been characterised and the most preferable sequences binding to octamers in three distinctive species have been identified. We are now ready to analyse the specific compositional properties of these DNA sequences. 

**Systematic evolution of ligands by exponential enrichment (SELEX)** is a method for identifying high affinity DNA binding sequences [1]. It is an iterative selection process that evolves a randomized pool of sequences into a high-affinity sub-population capable of binding to a specific target, and has been used previously to identify nucleosome binding sequences [2,3] .
SELEX begins with an initial DNA pool consisting of sequences with a variable binding region flanked by two constant regions that facilitate PCR amplification. An excess of this DNA library is mixed with the binding protein and bound complexes are isolated. The bound DNA is then extracted and amplified to produce a pool for the next round of selection that is enriched in binding sequences. Between five and fifteen rounds of selection and amplification are usually required for sufficient enrichment to obtain high-affinity binding sequences [4]. Once SELEX is completed, the molecules are characterized to identify characteristics in the sequences that affect binding.

![SELEX workflow for sample generation. Human mononucleosomal DNA was digested by MNase (1), the product was ligated with a 22-bp adapter and a 3’-overhanging thymine residue on both ends of sequence (2) then amplified and nucleosomes were <em>in vitro</em> reconstituted with recombinant histone octamers at 1:10 ratio of octamers to DNA (3). DNA was extracted from nucleosome bands in native PAGE (4) then re-amplified by PCR (5) for a total of 6 nucleosome selection rounds. The initial input and the outputs of rounds 1, 3 and 6 were sequenced. ](<img src="https://github.com/hientrinh93/SELEX/blob/master/workflow.png" width="200" height="400" />





