library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity I2C_FM_DESIGN is
    Port (
        clk_100MHz : in std_logic;    -- Reloj del sistema a 100 MHz
        rst : in std_logic;           -- Reset del sistema
        wr_enable : in std_logic;     -- Habilitación de escritura
        scl : out std_logic;          -- Línea de reloj I2C
        sda : inout std_logic         -- Línea de datos I2C (bidireccional)
    );
end I2C_FM_DESIGN;

architecture Behavioral of I2C_FM_DESIGN is

    -- Definición de los estados para la FSM del I2C
    type state is (st_idle, st_start, st_txSlaveAddress, st_ack0, st_txData, st_ack1, st_stop);
    signal present_state, next_state : state;

    -- Señales internas
    signal scl_buffer : std_logic := '1';
    signal sda_buffer : std_logic := '1';
    signal clk_div : integer range 0 to 99 := 0; -- Divisor de reloj para I2C

begin

    -- Proceso principal de la FSM
    process(clk_100MHz, rst)
    begin
        if rst = '1' then
            present_state <= st_idle;
            clk_div <= 0;
            scl_buffer <= '1';
            sda_buffer <= '1';
        elsif rising_edge(clk_100MHz) then
            -- Divisor de frecuencia para generar scl de 100 kHz desde 100 MHz
            if clk_div < 49 then
                clk_div <= clk_div + 1;
            else
                clk_div <= 0;
                scl_buffer <= not scl_buffer; -- Generación de SCL
            end if;

            -- FSM para el protocolo I2C
            case present_state is
                when st_idle =>
                    if wr_enable = '1' then
                        next_state <= st_start;
                    end if;

                when st_start =>
                    sda_buffer <= '0'; -- Condición de inicio (START)
                    next_state <= st_txSlaveAddress;

                when st_txSlaveAddress =>
                    -- Lógica para enviar la dirección del esclavo
                    -- Aquí agregas el código para enviar la dirección bit por bit
                    next_state <= st_ack0;

                when st_ack0 =>
                    -- Espera el ACK del esclavo
                    -- Aquí agregas la lógica para verificar el ACK
                    next_state <= st_txData;

                when st_txData =>
                    -- Lógica para enviar los datos
                    -- Aquí agregas el código para enviar los datos bit por bit
                    next_state <= st_ack1;

                when st_ack1 =>
                    -- Espera el segundo ACK
                    -- Lógica para verificar el segundo ACK
                    next_state <= st_stop;

                when st_stop =>
                    sda_buffer <= '1'; -- Condición de paro (STOP)
                    next_state <= st_idle;

                when others =>
                    next_state <= st_idle;
            end case;
            present_state <= next_state;
        end if;
    end process;

    -- Asignación de salidas
    scl <= scl_buffer;
    sda <= sda_buffer when (present_state /= st_idle) else 'Z';

end Behavioral;

