pc()
{ 
    ip_expr="$1"
    if [[ $# -eq 0 || $1 = '-' ]]; then
        read -r ip_expr
    fi
    python3.9 -c 'print('"$ip_expr"')'
}
