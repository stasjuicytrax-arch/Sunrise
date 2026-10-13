# Собирает видео из частей (_parts) в public/video и копирует PDF. Запускать из корня проекта.
$ErrorActionPreference = "Stop"
$names = "v1-aftermovie-loop","v1-aftermovie-full","v2-aftermovie-9x16-full","v3-spaceplus-full","v4-clubnight-full","v5-shortfilm-full"
foreach ($n in $names) {
  $parts = Get-ChildItem "_parts" -Filter "$n.mp4.part*" | Sort-Object Name
  if ($parts.Count -eq 0) { Write-Host "Нет частей для $n"; continue }
  $out = [System.IO.File]::Create("public\video\$n.mp4")
  foreach ($p in $parts) { $b = [System.IO.File]::ReadAllBytes($p.FullName); $out.Write($b, 0, $b.Length) }
  $out.Close()
  Write-Host "OK $n.mp4"
}
Copy-Item "..\..\PromoKit SunRise.pdf" "public\PromoKit-SunRise.pdf" -Force
Write-Host "OK PDF"
Remove-Item "_parts" -Recurse -Force
Write-Host "Готово"
