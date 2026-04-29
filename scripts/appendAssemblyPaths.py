import os
import sys

genomes = {}
with open(sys.argv[1]) as oasgf: # assembly_summary_genbank.txt - downloaded from NCBI: https://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_genbank.txt
    for line in oasgf:
        if line.startswith('#'): continue
        line = line.strip('\n')
        assembly_accession, bioproject, biosample, wgs_master, refseq_category, taxid, species_taxid, organism_name, infraspecific_name, isolate, version_status, assembly_level, release_type, genome_rep, seq_rel_date, asm_name, asm_submitter, gbrs_paired_asm, paired_asm_comp, ftp_path, excluded_from_refseq, relation_to_type_material, asm_not_live_date, assembly_type, group, genome_size, genome_size_ungapped, gc_percent, replicon_count, scaffold_count, contig_count, annotation_provider, annotation_name, annotation_date, total_gene_count, protein_coding_gene_count, non_coding_gene_count, pubmed_id = line.split('\t')
        try:
            genome = ftp_path + '/' + ftp_path.split('/')[-1] + '_genomic.fna.gz'
            gca_no_version = assembly_accession.split('.')[0]
            genomes[assembly_accession] = genome
            genomes[gca_no_version] = genome
        except:
            pass

with open(sys.argv[2]) as ogf:
    for i, line in enumerate(ogf):
        line = line.strip('\n')
        if i == 0:
            print(line + '\tgenome\tversion_match')
            continue
        gca, genus, species = line.split('\t')
        genome = 'NA'
        gca_no_vers = gca.split('.')[0]
        version_match = "False"
        if gca in genomes:
            genome = genomes[gca]
            version_match = "True"
        elif gca_no_vers in genomes:
            genome = genomes[gca_no_vers]
        
        print(line + '\t' + genome + '\t' + version_match)
