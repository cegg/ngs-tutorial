import vcf

v = vcf.Reader(filename='genotypes.vcf.gz')

rec = next(v)
print(rec.CHROM, rec.POS, rec.ID, rec.REF, rec.ALT, 
rec.QUAL, rec.FILTER)
print(rec.INFO)
print(rec.FORMAT)
samples = rec.samples
print(len(samples))
sample = samples[0]
print(sample.called, sample.gt_alleles, sample.is_het, 
sample.phased)
print(int(sample['DP']))