#theme colors(dynamic)
#default colors
light_green_1  = "#EDFBE3"
light_green_2  = "#b1ffad"
light_green_3  = "#b1ffad"
light_green_4  = "#98FB98"
light_green_5  = "#63C566"
green_1        = "#36D039"
green_2        = "#2CA52E"
green_3        = "#2CA52E"
green_4        = "#27BE31"
green_5        = "#00ff0d"
dark_green_1   = "#117118"
dark_green_2   = "#107116"
dark_green_3   = "#14721A"
dark_green_4   = "#1F7620"
dark_green_5   = "#0D540F"
dark_green_6   = "#0B4E10"

def get_current_color():
    if(light_green_1 == "#EDFBE3"): return "سبز"
    elif(light_green_1 == "#E3F2FD"): return "آبی"
    elif(light_green_1 == "#FFFDE7"): return "زرد"
    elif(light_green_1 == "#EFEBE9"): return "قهوه‌ای"
    elif(light_green_1 == "#F3E5F5"): return "بنفش"
    elif(light_green_1 == "#FFF3E0"): return "نارنجی"
    elif(light_green_1 == "#FFEBEE"): return "قرمز"
    elif(light_green_1 == "#FFFFFF"): return "طوسی"
    elif(light_green_1 == "#FFE0E9"): return "صورتی"
    else: return None
def get_theme_colors(selected_color):
    if selected_color == "green":
        return (
            "#EDFBE3", "#b1ffad", "#b1ffad", "#98FB98", "#63C566",
            "#36D039", "#2CA52E", "#2CA52E", "#27BE31", "#00ff0d",
            "#117118", "#107116", "#14721A", "#1F7620", "#0D540F", "#0B4E10"
        )
    elif selected_color == "blue":
        return (
            "#E3F2FD", "#B3E5FC", "#B3E5FC", "#AFEEEE", "#64B5F6",
            "#42A5F5", "#2196F3", "#2196F3", "#1E88E5", "#00B0FF",
            "#1565C0", "#1976D2", "#1A237E", "#283593", "#0D47A1", "#0B3D91"
        )
    elif selected_color == "yellow":
        return (
            "#FFFDE7", "#FFF59D", "#FFF59D", "#FFF176", "#FFE082",
            "#FFD600", "#FFEB3B", "#FFEB3B", "#FBC02D", "#FFD600",
            "#FFA000", "#FFB300", "#FF8F00", "#FF6F00", "#FFC107", "#FF9800"
        )
    elif selected_color == "brown":
        return (
            "#EFEBE9", "#D7CCC8", "#D7CCC8", "#BCAAA4", "#A1887F",
            "#8D6E63", "#A0522D", "#A0522D", "#6D4C41", "#795548",
            "#5D4037", "#4E342E", "#3E2723", "#532E21", "#3B1F12", "#2D1407"
        )
    elif selected_color == "purple":
        return (
            "#F3E5F5", "#E1BEE7", "#E1BEE7", "#CE93D8", "#BA68C8",
            "#AB47BC", "#9C27B0", "#9C27B0", "#8E24AA", "#7C4DFF",
            "#6A1B9A", "#512DA8", "#4527A0", "#311B92", "#4A148C", "#2D083B"
        )
    elif selected_color == "orange":
        return (
            "#FFF3E0", "#FFCC80", "#FFCC80", "#FFB74D", "#FFA726",
            "#FF9800", "#FFB300", "#FFB300", "#FB8C00", "#FFA500",
            "#F57C00", "#EF6C00", "#E65100", "#BF360C", "#9C3D00", "#7B2700"
        )
    elif selected_color == "red":
        return (
            "#FFEBEE", "#FFCDD2", "#FFCDD2", "#EF9A9A", "#E57373",
            "#EF5350", "#F44336", "#F44336", "#E53935", "#FF1744",
            "#D32F2F", "#C62828", "#B71C1C", "#8B0000", "#7C0A02", "#5A0002"
        )
    elif selected_color == "gray":
        return (
            "#FFFFFF", "#F5F5F5", "#EEEEEE", "#E0E0E0", "#CCCCCC",
            "#BDBDBD", "#9E9E9E", "#757575", "#616161", "#424242",
            "#303030", "#212121", "#111111", "#0A0A0A", "#050505", "#000000" 
        )
    elif selected_color == "pink":
        return (
            "#FFE0E9", "#FFCCD5", "#FFB3C6", "#FDA6BC", "#FF91AD",
            "#FF81A0", "#FF678D", "#FF507C", "#FF3E6E", "#FF245B",
            "#A33C9C", "#8A2A97", "#691A85", "#4F0C69", "#4E0070", "#4D0051"
        )     
    else:
        return ()

def set_theme_colors(selected_color):
    colors = get_theme_colors(selected_color)
    for i in range(5): globals()[f'light_green_{i+1}'] = colors[i]
    for i in range(5): globals()[f'green_{i+1}'] = colors[i + 5]
    for i in range(6): globals()[f'dark_green_{i+1}'] = colors[i + 10]
    
#text and background colors(Fixed)
white              = "#FFFFFF"
light_gray_1     = "#f1f1f1"
light_gray_2      = "#f6f6f6"
light_gray_3         = "#e3e3e3"
light_gray_4    = "#eaeaea"
light_gray_5   = "#ECECEC"
light_gray_6   = "#d9d9d9"
light_gray_7   = "#BDBDBD"
gray_1        = "#a2a2a2"
gray_2    = "#a9a9a9"
gray_3        = "#808080"
dark_gray_color   = "#5E5E5E"
black              = "#000000"
red_color = "#ff0000"
light_red_color = "#ff7979"
blue_color="#6BB1EE"