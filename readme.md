# SDXL Turbo Pipeline: A Lightweight Module for Lilypad

This README provides instructions for running the SDXL Turbo Pipeline module on the Lilypad network via the Lilypad CLI. Learn about installing the CLI here: https://docs.lilypad.tech/lilypad/lilypad-testnet/install-run-requirements

## Prerequisites

- Lilypad CLI installed (for Lilypad network runs)

If you would like to run this Lilypad module locally using the Lilypad localnet
- Docker installed on your system
- GPU

## Running on Lilypad Network

### Using Lilypad LocalNet

To run on the local development network:

```
go run . run --network dev github.com/Lilypad-Tech/module-sdxl:d6a89ed92f4e798459b2990340669da00c56c80c--web3-private-key <admin_key> -i prompt="your prompt here"
```

Replace `<admin_key>` with the admin key found in `hardhat/utils/accounts.ts`.

Example:
```
go run . run --network dev github.com/Lilypad-Tech/module-sdxl:d6a89ed92f4e798459b2990340669da00c56c80c --web3-private-key <admin_key> -i prompt="a spaceship parked on mountain"
```

### Using Lilypad Main Network

To run on the main Lilypad network:

```
lilypad run github.com/Lilypad-Tech/module-sdxl:d6a89ed92f4e798459b2990340669da00c56c80c -i prompt="your prompt here"
```

Example:
```
lilypad run github.com/Lilypad-Tech/module-sdxl:d6a89ed92f4e798459b2990340669da00c56c80c -i prompt="a spaceship parked on mountain"
```

## Notes

- Ensure you have the necessary permissions and resources to run Docker containers with GPU support.
- The module version (`ae17e969cadab1c53d7cabab1927bb403f02fd2a`) may be updated. Check for the latest version before running.
- Adjust port mappings and volume mounts as needed for your specific setup.

![output](https://github.com/user-attachments/assets/fd15fd70-f543-48c6-b5e7-2d5d835edd78)
