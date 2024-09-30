import arcpy

# Parâmetros de entrada
nome_propriedade = arcpy.GetParameterAsText(0)
input_propriedade = arcpy.GetParameterAsText(1)
input_FT_base_edicao = arcpy.GetParameterAsText(2)
input_APP = arcpy.GetParameterAsText(3)
input_RPA8_1_500 = arcpy.GetParameter(4)
output_dataset = arcpy.GetParameterAsText(5)

# 1. Clip da camada 'FT_base_Edicao'
output_clip_FT_base = arcpy.analysis.Clip(input_FT_base_edicao, input_propriedade, output_dataset + "\\" + nome_propriedade + "_FT_base_Edicao")

# 2. Clip da camada 'input_APP'
output_clip_APP = arcpy.analysis.Clip(input_APP, input_propriedade, output_dataset + "\\" + nome_propriedade + "_APP")

# 2.1. Clip do resultado de codgeo_APP - DENTRO_APP
output_clip_DENTRO_APP = arcpy.analysis.Clip(output_clip_FT_base, output_clip_APP, output_dataset + "\\" + nome_propriedade + "_FT_base_DENTRO_APP")

# Atualizar campo "obs" com "dentro de APP" em DENTRO_APP
arcpy.management.AddField(output_clip_DENTRO_APP, "obs", "TEXT")
arcpy.management.CalculateField(output_clip_DENTRO_APP, "obs", "'dentro de APP'", "PYTHON")

# 2.2. Erase do resultado de codgeo_APP - FORA_APP
output_erase_FORA_APP = arcpy.analysis.Erase(output_clip_FT_base, output_clip_APP, output_dataset + "\\" + nome_propriedade + "_FT_base_FORA_APP")

# Atualizar campo "obs" com "fora de APP" em FORA_APP
arcpy.management.AddField(output_erase_FORA_APP, "obs", "TEXT")
arcpy.management.CalculateField(output_erase_FORA_APP, "obs", "'fora de APP'", "PYTHON")

#Export FORA_APP - codgeo_FT_base_Analises
output_merge_FT_base_Analises = arcpy.conversion.ExportFeatures(output_erase_FORA_APP, output_dataset + "\\" + nome_propriedade + "_FT_base_Analises")
#Append DENTRO APP para codgeo_FT_base_Analises
arcpy.management.Append(output_clip_DENTRO_APP, output_merge_FT_base_Analises, "NO_TEST")

# 3. Merge entre DENTRO_APP e FORA_APP : codgeo_FT_base_Analises
#output_merge_FT_base_Analises = arcpy.management.Merge([output_clip_DENTRO_APP, output_erase_FORA_APP], output_dataset + "\\" + nome_propriedade + "_FT_base_Analises")

# 4 Obtendo codgeo_REMAP_RPA08
output_clip_REMAP_RPA8 = arcpy.analysis.Clip(input_RPA8_1_500, input_propriedade, output_dataset + "\\" + nome_propriedade + "_REMAP_RPA08")

# 5 Obtendo codgeo_REMAP_RPA08_Erase_Base_Analise
output_REMAP_RPA8_erase = arcpy.analysis.Erase(output_clip_REMAP_RPA8, output_merge_FT_base_Analises, output_dataset + "\\" + nome_propriedade + "_REMAP_RPA08_Erase_Base_Analise")

# 5.1 codgeo_REMAP_Base_DENTRO_APP
output_clip_REMAP_RPA8_DENTRO_APP = arcpy.analysis.Clip(output_REMAP_RPA8_erase, output_clip_APP, output_dataset + "\\" + nome_propriedade + "_REMAP_RPA08_Base_DENTRO_APP")
# Atualizar campo "obs" com "dentro de APP" em DENTRO_APP
arcpy.management.AddField(output_clip_REMAP_RPA8_DENTRO_APP, "obs", "TEXT")
arcpy.management.CalculateField(output_clip_REMAP_RPA8_DENTRO_APP, "obs", "'dentro de APP'", "PYTHON")

# 5.2 codgeo_REMAP_Base_FORA_APP
output_erase_REMAP_RPA8_FORA_APP = arcpy.analysis.Erase(output_REMAP_RPA8_erase, output_clip_REMAP_RPA8_DENTRO_APP, output_dataset + "\\" + nome_propriedade + "_REMAP_RPA08_Base_FORA_APP")
arcpy.management.AddField(output_erase_REMAP_RPA8_FORA_APP, "obs", "TEXT")
arcpy.management.CalculateField(output_erase_REMAP_RPA8_FORA_APP, "obs", "'fora de APP'", "PYTHON")

# Append para codgeo_FT_Base_Analises
arcpy.management.Append(output_erase_REMAP_RPA8_FORA_APP, output_merge_FT_base_Analises, "NO_TEST")
arcpy.management.Append(output_clip_REMAP_RPA8_DENTRO_APP, output_merge_FT_base_Analises, "NO_TEST")
# Atualizar o "Código Geo Propriedade"
arcpy.management.AddField(output_merge_FT_base_Analises, "prop_select", "TEXT")
arcpy.management.CalculateField(output_merge_FT_base_Analises, "prop_select", "'{}'".format(nome_propriedade), "PYTHON")

