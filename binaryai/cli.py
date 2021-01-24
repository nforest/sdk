#!/usr/bin/env python
import os
import click
import platform
import binaryai

# diff between py2 and py3
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


def get_user_idadir():
    system = platform.system()
    if system == 'Windows':
        return os.path.join(os.getenv('APPDATA'), "Hex-Rays", "IDA Pro")
    elif system in ['Linux', 'Darwin']:
        return os.path.join(os.getenv('HOME'), ".idapro")
    else:
        return ""


def get_plugin_path():
    return os.path.join(os.path.abspath(os.path.join(binaryai.__file__, os.path.pardir)), "ida_binaryai.py")


@click.group(invoke_without_command=True)
@click.option('--help', '-h', is_flag=True, help='show this message and exit.')
@click.option('--version', '-v', is_flag=True, help='show version')
@click.pass_context
def cli(ctx, help, version):
    if ctx.invoked_subcommand is None or help:
        if version:
            click.echo(binaryai.__version__)
            ctx.exit()
        else:
            banner = r'''
 ____  _                           _    ___
| __ )(_)_ __   __ _ _ __ _   _   / \  |_ _|
|  _ \| | '_ \ / _` | '__| | | | / _ \  | |
| |_) | | | | | (_| | |  | |_| |/ ___ \ | |
|____/|_|_| |_|\__,_|_|   \__, /_/   \_\___|
                          |___/
        '''
            click.echo(banner)
            click.echo(ctx.get_help())
            ctx.exit()


@cli.command('install_ida_plugin', short_help='install IDA plugin')
@click.option('--directory', '-d', help='IDA plugin directory', type=click.Path(), default=None)
@click.pass_context
def InstallPlugin(ctx, directory):
    if directory and not os.path.isdir(directory):
        click.echo('Invalid plugin path')
        ctx.exit()
    if not directory:
        directory = os.path.join(get_user_idadir(), 'plugins')
        os.makedirs(directory) if not os.path.exists(directory) else None
    plugin_path = os.path.join(directory, 'ida_binaryai.py')
    click.echo("Installing ida_binaryai.py into {}".format(directory))
    plugin_code = """# auto-generated by `binaryai install_ida_plugin`
def PLUGIN_ENTRY():
    from binaryai import ida_binaryai
    return ida_binaryai.BinaryAIIDAPlugin()
"""
    try:
        with open(plugin_path, "w") as f:
            f.write(plugin_code)
    except Exception:
        click.echo("Error while installing ida_binaryai.py.")
        ctx.exit()
    click.echo("Done")


def main():
    cli()
