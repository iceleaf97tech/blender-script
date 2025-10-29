import bpy

obj = bpy.context.active_object

if obj and obj.type == 'MESH':
    mesh = obj.data
    uv_layers = mesh.uv_layers
    
    if len(uv_layers) >= 2:
        print("開始交換UV數據...")
        
        # 保存兩個通道的名稱
        name0 = uv_layers[0].name
        name1 = uv_layers[1].name
        
        # 創建臨時UV層來保存channel 0的數據
        temp_uv = uv_layers.new(name="temp_swap")
        
        # 複製channel 0到temp
        for i in range(len(mesh.loops)):
            temp_uv.data[i].uv = uv_layers[0].data[i].uv.copy()
        
        # 複製channel 1到channel 0
        for i in range(len(mesh.loops)):
            uv_layers[0].data[i].uv = uv_layers[1].data[i].uv.copy()
        
        # 複製temp到channel 1
        for i in range(len(mesh.loops)):
            uv_layers[1].data[i].uv = temp_uv.data[i].uv.copy()
        
        # 刪除臨時UV層
        uv_layers.remove(temp_uv)
        
        # 恢復名稱
        uv_layers[0].name = name1
        uv_layers[1].name = name0
        
        print("UV數據交換完成！")
        print(f"Channel 0: {uv_layers[0].name}")
        print(f"Channel 1: {uv_layers[1].name}")
    else:
        print(f"需要至少2個UV通道，當前只有 {len(uv_layers)} 個")
else:
    print("請選擇一個Mesh物體")
