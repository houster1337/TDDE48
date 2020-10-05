# Read me

Presets for different network conditions.

## 4G

``` python
setConditions(delay=50, downloadMb=50, uploadMb=10)
*Results*
Mean buffer size: 62.413055555555545
Mean network activity: 81.52777777777777
```

## 3G

``` python
setConditions(delay=100, downloadMb=0.78, uploadMb=0.33)
```

*Results*
Mean buffer size: 39.62711111111112
Mean network activity: 22.727777777777778

## Very bad, but no packet loss

``` python
setConditions(delay=500, downloadMb=1, uploadMb=1)
```

*Results*
Mean buffer size: 35.86933333333333
Mean network activity: 45.605555555555554
