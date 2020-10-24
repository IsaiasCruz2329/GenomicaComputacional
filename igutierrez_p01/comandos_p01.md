# Comandos de la Practica 01
## Abel Isaias Gutierrez Cruz 

# Parte I. 

**Respuesta 1:**
echo $SHELL 
/bin/bash

**Respuesta 2:**
mkdir data/ filtered/ raw_data/ meta/ scripts/ figures/ archive/

**Respuesta 3:**
mv filtered/ data && mv raw_data/ data

**Respuesta 4:**
Directorio | Función 
--- | ---
**data** | Contiene los datos que se desean analizar. Puede estar dividido en otros directorios segun la naturaleza de los datos o su estado de procesamiento. Ejemplo:  1. raw  2. filtered 
**meta** | Directorio en donde se pueden guardar los metadatos, como un archivo cvs detallando información de cada una de las muestras. 
**scripts** | Dirección en donde se guardan los scripts necesarios para llevar a cabo el análisis de principio a fin. 
**figures** | Este directorio es una variante de "scripts" ya que aquí se guarda el codigo utilizado para hacer las figuras de una publicación dada. 
**archive** | Este directorio no se sube al repositorio, pero es bueno usarlo para scripts o resultados que no estemos completamente seguros de necesitarlos o no.

# Parte II. 

**Respuesta 1:**
chmod u+x delay.sh

**Respuesta 2:**
ls -l
./delay.sh

**Respuesta 3:**
'#! /bin/bash
echo "Después de la Parte I. necesito un descanso de exactamente 30 segundos."
sleep 30
echo "Ya puedo continuar"'

**Respuesta 4:**
./delay.sh &
kill -9 47808

# Parte III. 

**Respuesta 1:**
wc -w SarsCov-2.txt

**Respuesta 2:**
mv /home/isaias/Descargas/sequence.fasta sarscov2_genome.fasta
mv /home/isaias/Descargas/sequence.fasta splike_c.faa

# Parte IV. 

**Respuesta 1:**
ln -s ~/../raw_data/splike_c.faa
ln -s ~/../raw_data/splike_b.faa
ln -s ~/../raw_data/splike_a.faa

**Respuesta 2:**

touch glycoproteins.faa

**Respuesta 3:**
head -n1 splike_a.faa >> ../filtered/glycoproteins.faa
>pdb|6VXX|A Chain A, SARS-CoV-2 spike glycoprotein
>pdb|6VXX|B Chain B, SARS-CoV-2 spike glycoprotein
>pdb|6VXX|C Chain C, SARS-CoV-2 spike glycoprotein

**Respuesta 4:**

less splike_c.faa >> ../filtered/glycoproteins.faa

**Respuesta 5:**
mv splike_c.faa ../../archive/

**Respuesta 6:**
head -n3 sarscov2_genome.fasta

>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC

zless sarscov2_assembly.fasta.gz | head -n3

>NODE_1_length_264_cov_161.042781
CACAAATCTTAACACTCTTCCCTACACGACGCTCTTCCGATCTACGCCGGGCCATTCGTA
CGAACCGATACCTGTGGTAAAGGGTCCTACTGTATGGTGGTACACGAGTAGTAGCAAATG

**Respuesta 7:**
grep '>' sarscov2_genome.fasta | wc -l
1 

zless sarscov2_assembly.fasta.gz | grep '>' | wc -l
35

**Respuesta 8:**

zless SRR10971381_R2.fastq.gz | head -n12
@SRR10971381.512_2
CGTGGAGTATGGCTACATACTACTTATTTGATGAGTCTGGTGAGTTTAAAGTGGCTTCACATATGTATTGTTCTTTCTACCCTCCAGATGAGGATGAAGAAGAAGGTGATTGTGAAGAAGAAGAGTTTGAGCCATCAACTCAATATGAGT
+
/FFFA/A/FFFF66FFFFFF/FF/FFFFFFFFFFFFF/AFFF6FFFA6FFFFF/FFFFFFFFFFFFFFFFFF/FF/FFFFFA/FFF/FFF/A/AFA/FFFFF/=F/F/F/AFAFF//A/AFF//FFAF/FFF=FFAFFFA/A/6=///==
@SRR10971381.556_2
TTTGTAAAAATAAAATAAAAAAAATAAAAATAATATATTAAAAAAAGATAAATAAAAAAATGAACAATTAATAAAAAAAAAAAAAAAAAAAAATTAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAATAAAAAAAAAATTATAAAA
+
6AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF/FFFAFFFFFF/FFA/FF=F//=FF/FFFFFFFFFFFFFA/FFFF/FF/FA//F/FFFFFFA/=FFFFF/FFFF/F=FFFAFF///FFFFA/FF/6//////=/
@SRR10971381.1428_2
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
+
FFFFFFFFFFFFAFFFAFFFFFF6A//F//FFF

zless SRR10971381_R2.fastq.gz | grep '@' | wc -l
130022

**Respuesta 9:**
En cuanto al formata faa contienen secuencias de aminoacidos, los archivos fasta contienen secuencias de nucleotidos. El formato almacena datos de nucleotidos, pero por cada uno de ellos tiene un valor de calidad

**Respuesta 10:**
La diferencia es que con el comando -S muestra las lineas completas, además que acomodarlas conforme a cada columna presente en el archivo 

**Respuesta 11:**

less -S sarscov2_genome.gff3 | cut -f3 | grep 'gene' | wc -l
11
