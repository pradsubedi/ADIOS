adios_groupsize = 4 + 4 + 4 + 4 + 4*(size)*(NY) + 4*(size)*(NY) + 4*(size)*(NY) + 4*(size)*(NY);
adios_group_size(adios_handle, adios_groupsize, &adios_totalsize, &group_comm);
adios_write(adios_handle,"NX",&NX);
adios_write(adios_handle,"NY",&NY);
adios_write(adios_handle,"offset",&offset);
adios_write(adios_handle,"size",&size);
adios_write(adios_handle,"data",u+offset*NY);
adios_write(adios_handle,"cos_data",cos_u[offset]);
adios_write(adios_handle,"sin_data",sin_u[offset]);
adios_write(adios_handle,"tan_data",tan_u[offset]);
