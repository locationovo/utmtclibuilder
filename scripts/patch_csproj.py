#!/usr/bin/env python3
"""Patch csproj for iOS NativeAOT with trimmed metadata."""

import sys
import os
import xml.etree.ElementTree as ET

IOS_PROPS = {
    'TargetFramework': 'net10.0-ios',
    'RuntimeIdentifier': 'ios-arm64',
    'PublishAot': 'true',
    'PublishAotUsingRuntimePack': 'true',
    'DisableUnsupportedError': 'true',
    'IlcGenerateCompleteTypeMetadata': 'false',
    'IlcTrimMetadata': 'true',
    'IlcDisableReflection': 'false',
    'IlcOptimizationPreference': 'Speed',
    'IlcFoldIdenticalMethodBodies': 'true',
    'PublishTrimmed': 'true',
    'MtouchLink': 'None',
    'UseInterpreter': 'false',
    'UseMonoRuntime': 'false',
    'SupportedOSPlatformVersion': '13.0',
    'ApplicationId': 'com.utmt.cli',
    'ApplicationTitle': 'UndertaleModCli',
    'ApplicationVersion': '1.0.0',
    'ApplicationDisplayVersion': '1.0',
    'CFBundleIdentifier': 'com.utmt.cli',
    'CFBundleName': 'UndertaleModCli',
    'CFBundleDisplayName': 'UndertaleModCli',
    'CFBundleVersion': '1',
    'CFBundleShortVersionString': '1.0',
    'NoWarn': 'IL2026;IL3050;IL2070;IL2075;IL2065',
}


def ns_of(root):
    return root.tag.split('}')[0] + '}' if root.tag.startswith('{') else ''


def pick_group(root, ns):
    groups = root.findall(f'{ns}PropertyGroup')
    for g in groups:
        if g.find(f'{ns}TargetFramework') is not None:
            return g
    return groups[0] if groups else ET.SubElement(root, f'{ns}PropertyGroup')


def set_props(group, ns, props):
    for key, value in props.items():
        el = group.find(f'{ns}{key}')
        if el is None:
            el = ET.SubElement(group, f'{ns}{key}')
        el.text = value


def patch_main(path):
    tree = ET.parse(path)
    root = tree.getroot()
    ns = ns_of(root)
    set_props(pick_group(root, ns), ns, IOS_PROPS)
    tree.write(path, encoding='utf-8', xml_declaration=True)
    print(f'Main: {path}')


def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <main.csproj>', file=sys.stderr)
        return 1
    patch_main(sys.argv[1])
    return 0


if __name__ == '__main__':
    sys.exit(main())