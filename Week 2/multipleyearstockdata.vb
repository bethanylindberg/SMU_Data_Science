Sub stockdata()
Dim ticker As String
Dim volume As Double
Dim lastrow As Long
Dim summarytablerow As Integer
Dim yearopen As Double
Dim yearclose As Double
Dim yearlychange As Double
Dim worksheet_count As Integer

worksheet_count = ThisWorkbook.Worksheets.Count
volume = 0

For y = 1 To worksheet_count
Worksheets(y).Activate

    'Set headers for summary table
    Range("I1").Value = "Ticker"
    Range("J1").Value = "Yearly Change"
    Range("K1").Value = "Percent Change"
    Range("L1").Value = "Total Stock Volume"
    summarytablerow = 2
    lastrow = Cells(Rows.Count, 1).End(xlUp).Row

        For x = 2 To lastrow
        
            'check if ticker was traded
            If Cells(x, 7) <> 0 Then
               'Preserve open value
               Do While IsEmpty(Range("K" & summarytablerow))
               Range("K" & summarytablerow).Value = Cells(x, 3).Value
               Loop
            End If

                If Cells(x + 1, 1).Value <> Cells(x, 1).Value Then 'if not in the same ticker
                    ticker = (Cells(x, 1)) 'set ticker
                    yearclose = (Cells(x, 6)) 'set close
                    yearopen = (Cells(summarytablerow, 11)) 'set open
                    yearlychange = yearclose - yearopen 'calculate change
                    volume = volume + Cells(x, 7) ' add to volume
                    Range("I" & summarytablerow).Value = ticker 'add ticker to summary table
                    Range("J" & summarytablerow).Value = yearlychange 'add yearlychange to summary table
                        If yearopen = 0 Then
                            Range("K" & summarytablerow).Value = 0
                        Else
                            Range("K" & summarytablerow).Value = yearlychange / yearopen 'calculate percentage change
                        End If
                    Range("L" & summarytablerow).Value = volume 'add volume to summary table
                    summarytablerow = summarytablerow + 1 'add one to summary table row
                    volume = 0 'reset volume for next ticker
                Else 'if in same ticker
                    volume = volume + Cells(x, 7).Value 'add to volume
                End If
                
        Next x
   
   'subtract extra row
    summarytablerow = summarytablerow - 1
    
    'Format columns of summary table
    Range("J2:J" & summarytablerow).NumberFormat = "0.000000000"
    Range("K2:K" & summarytablerow).NumberFormat = "0.00%"

    'Conditional formatting
    Range("J2:J" & summarytablerow).Select
    Selection.FormatConditions.Delete
    Set cond1 = Selection.FormatConditions.Add(xlCellValue, xlLess, "0")
    Set cond2 = Selection.FormatConditions.Add(xlCellValue, xlGreaterEqual, "0")
    With cond1
    .Interior.Color = vbRed
    End With
    With cond2
    .Interior.Color = vbGreen
    End With
    Range("A1").Select

    'Additional Headers
    Range("P1").Value = "Ticker"
    Range("Q1").Value = "Total Stock Volume"

    'Greatest % increase
    Range("O2").Value = "Greatest % increase"
    Range("Q2").Value = Application.WorksheetFunction.Max(Range("K2:K" & summarytablerow))
    Range("P2").Value = Application.WorksheetFunction.Index(Range("I1:L" & summarytablerow), Application.WorksheetFunction.Match(Range("Q2"), Range("K1:K" & summarytablerow), 0), Application.WorksheetFunction.Match(Range("P1"), Range("I1:L1"), 0))
    Range("Q2").NumberFormat = "0.00%"

    'Greatest % decrease
    Range("O3").Value = "Greatest % decrease"
    Range("Q3").Value = Application.WorksheetFunction.Min(Range("K2:K" & summarytablerow))
    Range("P3").Value = Application.WorksheetFunction.Index(Range("I1:L" & summarytablerow), Application.WorksheetFunction.Match(Range("Q3"), Range("K1:K" & summarytablerow), 0), Application.WorksheetFunction.Match(Range("P1"), Range("I1:L1"), 0))
    Range("Q3").NumberFormat = "0.00%"

    'Greatest total volume
    Range("O4").Value = "Total Stock Volume"
    Range("Q4").Value = Application.WorksheetFunction.Max(Range("L2:L" & summarytablerow))
    Range("P4").Value = Application.WorksheetFunction.Index(Range("I1:L" & summarytablerow), Application.WorksheetFunction.Match(Range("Q4"), Range("L1:L" & summarytablerow), 0), Application.WorksheetFunction.Match(Range("P1"), Range("I1:L1"), 0))
    Range("Q1").Value = "Value"

    'Autofit
    Columns("I:Q").AutoFit

Next y

End Sub