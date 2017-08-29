"""
Windows Meta File
"""

from construct import *

wmf_record = Struct("records",
    ULInt32("size"), # size in words, including the size, function and params
    Enum(ULInt16("function"),
        AbortDoc = 0x0052,
        Aldus_Header = 0x0001,
        AnimatePalette = 0x0436,
        Arc = 0x0817,
        BitBlt = 0x0922,
        Chord = 0x0830,
        CLP_Header16 = 0x0002,
        CLP_Header32 = 0x0003,
        CreateBitmap = 0x06FE,
        CreateBitmapIndirect = 0x02FD,
        CreateBrush = 0x00F8,
        CreateBrushIndirect = 0x02FC,
        CreateFontIndirect = 0x02FB,
        CreatePalette = 0x00F7,
        CreatePatternBrush = 0x01F9,
        CreatePenIndirect = 0x02FA,
        CreateRegion = 0x06FF,
        DeleteObject = 0x01F0,
        DibBitblt = 0x0940,
        DibCreatePatternBrush = 0x0142,
        DibStretchBlt = 0x0B41,
        DrawText = 0x062F,
        Ellipse = 0x0418,
        EndDoc = 0x005E,
        EndPage = 0x0050,
        EOF = 0x0000,
        Escape = 0x0626,
        ExcludeClipRect = 0x0415,
        ExtFloodFill = 0x0548,
        ExtTextOut = 0x0A32,
        FillRegion = 0x0228,
        FloodFill = 0x0419,
        FrameRegion = 0x0429,
        Header = 0x0004,
        IntersectClipRect = 0x0416,
        InvertRegion = 0x012A,
        LineTo = 0x0213,
        MoveTo = 0x0214,
        OffsetClipRgn = 0x0220,
        OffsetViewportOrg = 0x0211,
        OffsetWindowOrg = 0x020F,
        PaintRegion = 0x012B,
        PatBlt = 0x061D,
        Pie = 0x081A,
        Polygon = 0x0324,
        Polyline = 0x0325,
        PolyPolygon = 0x0538,
        RealizePalette = 0x0035,
        Rectangle = 0x041B,
        ResetDC = 0x014C,
        ResizePalette = 0x0139,
        RestoreDC = 0x0127,
        RoundRect = 0x061C,
        SaveDC = 0x001E,
        ScaleViewportExt = 0x0412,
        ScaleWindowExt = 0x0410,
        SelectClipRegion = 0x012C,
        SelectObject = 0x012D,
        SelectPalette = 0x0234,
        SetBKColor = 0x0201,
        SetBKMode = 0x0102,
        SetDibToDev = 0x0D33,
        SelLayout = 0x0149,
        SetMapMode = 0x0103,
        SetMapperFlags = 0x0231,
        SetPalEntries = 0x0037,
        SetPixel = 0x041F,
        SetPolyFillMode = 0x0106,
        SetReLabs = 0x0105,
        SetROP2 = 0x0104,
        SetStretchBltMode = 0x0107,
        SetTextAlign = 0x012E,
        SetTextCharExtra = 0x0108,
        SetTextColor = 0x0209,
        SetTextJustification = 0x020A,
        SetViewportExt = 0x020E,
        SetViewportOrg = 0x020D,
        SetWindowExt = 0x020C,
        SetWindowOrg = 0x020B,
        StartDoc = 0x014D,
        StartPage = 0x004F,
        StretchBlt = 0x0B23,
        StretchDIB = 0x0F43,
        TextOut = 0x0521,
        _default_ = Pass,
    ),
    Array(lambda ctx: ctx.size - 3, ULInt16("params")),
)

wmf_placeable_header = Struct("placeable_header",
  Const(ULInt32("key"), 0x9AC6CDD7),
  ULInt16("handle"),
  SLInt16("left"),
  SLInt16("top"),
  SLInt16("right"),
  SLInt16("bottom"),
  ULInt16("units_per_inch"),
  Padding(4),
  ULInt16("checksum")
)

wmf_file = Struct("wmf_file",
    # --- optional placeable header ---
    Optional(wmf_placeable_header),

    # --- header ---
    Enum(ULInt16("type"),
        InMemory = 0,
        File = 1,
    ),
    Const(ULInt16("header_size"), 9),
    ULInt16("version"),
    ULInt32("size"), # file size is in words
    ULInt16("number_of_objects"),
    ULInt32("size_of_largest_record"),
    ULInt16("number_of_params"),

    # --- records ---
    GreedyRange(wmf_record)
)
