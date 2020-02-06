https://hub.packtpub.com/processing-next-generation-sequencing-datasets-using-python/

tabix -fh ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/supporting/vcf_with_sample_level_annotation/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5_extra_anno.20130502.genotypes.vcf.gz 22:1-17000000  | bgzip -c > genotypes.vcf.gzi

The first line will perform a partial download of the VCF file for chromosome 22 (up to 17 Mbp) of the 1000 genomes project. Then, bgzip will compress it.

The second line will create an index, which we will need for direct access to a section of the genome.
