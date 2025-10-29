import bpy

# 獲取當前選中的物體
obj = bpy.context.active_object

# 確認物體是mesh類型
if obj and obj.type == 'MESH':
    mesh = obj.data
    uv_layers = mesh.uv_layers
    
    # 檢查UV通道數量
    if len(uv_layers) == 0:
        print("錯誤: 沒有UV通道")
    elif len(uv_layers) == 1:
        # 只有一個通道，命名為 baseUV
        uv_layers[0].name = "baseUV"
        print(f"Channel 0 已重命名為: {uv_layers[0].name}")
    elif len(uv_layers) >= 2:
        # 有兩個或以上通道，分別命名
        uv_layers[0].name = "baseUV"
        uv_layers[1].name = "lightUV"
        print(f"Channel 0 已重命名為: {uv_layers[0].name}")
        print(f"Channel 1 已重命名為: {uv_layers[1].name}")
    
    # 顯示所有UV通道
    print(f"\n物體 '{obj.name}' 的UV通道總數: {len(uv_layers)}")
    for i, uv_layer in enumerate(uv_layers):
        print(f"  Channel {i}: {uv_layer.name}")
else:
    print("請選擇一個Mesh物體")
