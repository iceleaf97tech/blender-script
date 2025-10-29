import bpy

# 獲取當前選中的物體
obj = bpy.context.active_object

# 確認物體是mesh類型
if obj and obj.type == 'MESH':
    mesh = obj.data
    
    # 獲取UV層
    uv_layers = mesh.uv_layers
    
    print(f"物體 '{obj.name}' 的UV通道:")
    print(f"UV通道總數: {len(uv_layers)}")
    
    # 列出channel 0和1的名稱
    if len(uv_layers) > 0:
        print(f"Channel 0: {uv_layers[0].name}")
    else:
        print("Channel 0: 不存在")
    
    if len(uv_layers) > 1:
        print(f"Channel 1: {uv_layers[1].name}")
    else:
        print("Channel 1: 不存在")
    
    # 額外列出所有UV通道
    print("\n所有UV通道:")
    for i, uv_layer in enumerate(uv_layers):
        print(f"  Index {i}: {uv_layer.name}")
else:
    print("請選擇一個Mesh物體")
