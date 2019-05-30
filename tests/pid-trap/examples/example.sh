#!/usr/bin/env bash
{ set +x; } 2>/dev/null

sleep 5 &
pid-trap $! echo beep
