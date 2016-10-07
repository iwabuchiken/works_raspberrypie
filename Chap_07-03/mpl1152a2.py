import smbus
import time

def getpressur(ch):
    i2c = smbus.SMBus(ch)
    ADDRESS = (0x60)

    i2c.write_i2c_block_data(ADDRESS,(0x12),[0x12])

    time.sleep(0.5)

    p_m = i2c.read_byte_data(ADDRESS,(0x00))
    p_l = i2c.read_byte_data(ADDRESS,(0x01))
    t_m = i2c.read_byte_data(ADDRESS,(0x02))
    t_l = i2c.read_byte_data(ADDRESS,(0x03))
    a0_m = i2c.read_byte_data(ADDRESS,(0x04))
    a0_l = i2c.read_byte_data(ADDRESS,(0x05))
    b1_m = i2c.read_byte_data(ADDRESS,(0x06))
    b1_l = i2c.read_byte_data(ADDRESS,(0x07))
    b2_m = i2c.read_byte_data(ADDRESS,(0x08))
    b2_l = i2c.read_byte_data(ADDRESS,(0x09))
    c12_m = i2c.read_byte_data(ADDRESS,(0x0a))
    c12_l = i2c.read_byte_data(ADDRESS,(0x0b))

    padc = (p_m << 8 | p_l ) >> 6
    tadc = (t_m << 8 | t_l ) >> 6
    a0 = (float)( ( a0_m << 8 )  | a0_l ) / ( 2 << 3 )
    b1 = (float)( ( b1_m << 8 ) | b1_l ) / ( 2 << 13 )
    b2 = (float)( ( b2_m << 8 ) | b2_l ) / ( 2 << 14 )
    c12 = (float)( ( c12_m << 8 ) | ( c12_l >> 2 ) ) / ( 2 << 13 )

    pcomp = a0 + ( b1 + c12 * tadc ) * padc + b2 * tadc

    pout = ( pcomp * 65 / 1023 + 50 ) / 10
   
    return pout
