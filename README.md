# further-promohub-scripts
python scraping scripts for further-promohub repository



# Environment instantiation:

Create .\envs subdirectory at the highest level within the project directory

Run the command:

    conda env create -f environment.yml --prefix .\envs

    conda activate further-promohub


Once activated, if the environment prefix (absolute/path/to/envs) $ is too long, run this command to edit your .condarc (the file that effects all conda environments). This will change the environment prefix to just (the environment name)

    conda config --set env_prompt '({name})'

        - note, yes, type '({name})' verbatim.

