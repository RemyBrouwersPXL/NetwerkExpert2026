from netmiko import ConnectHandler

# Definieer de routergegevens. Pas wachtwoord aan indien nodig.
router = {
    'device_type': 'cisco_ios',
    'host': '192.168.11.1',
    'username': 'student',
    'password': 'cisco123',
}

try:
    print("Verbinding maken met de router...")
    # Oefening 2.4a: Verbinding maken
    net_connect = ConnectHandler(**router)
    
    # Oefening 2.4b: Informatie ophalen
    output = net_connect.send_command("show ip interface brief")
    
    print("\n--- Ruwe Output ---")
    print(output)
    print("\n" + "="*40 + "\n")
    
    # Oefening 3.1 & 3.2: Tellers initialiseren
    up_count = 0
    down_count = 0
    admin_down_count = 0
    
    print("--- Interface Namen en Status ---")
    
    # Splits de output in losse regels en sla de eerste regel (de header) over
    lines = output.strip().split('\n')[1:] 
    
    for line in lines:
        parts = line.split()
        if len(parts) >= 4:
            # Oefening 3.3: Naam van de interface
            interface_name = parts[0] 
            
            # Controleer de status en tel op
            if "administratively down" in line:
                admin_down_count += 1
                print(f"{interface_name} is Administratively Down")
            elif "up" in parts[4]: # Kolom 4 is de status kolom
                up_count += 1
                print(f"{interface_name} is Up")
            elif "down" in parts[4]:
                down_count += 1
                print(f"{interface_name} is Down")
                
    # Samenvatting printen
    print("\n--- Eindtelling ---")
    print(f"UP: {up_count}")
    print(f"DOWN: {down_count}")
    print(f"ADMINISTRATIVELY DOWN: {admin_down_count}")
    
    # Verbreek de verbinding netjes
    net_connect.disconnect()

except Exception as e:
    print(f"Fout tijdens het uitvoeren: {e}")