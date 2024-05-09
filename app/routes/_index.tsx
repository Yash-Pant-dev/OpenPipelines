import type { MetaFunction } from "@remix-run/node";
import { Link } from "@remix-run/react";
import { Button } from "~/components/ui-library/button";
import { Input } from "~/components/ui-library/input";
import { Label } from "~/components/ui-library/label";
import { LoaderFunctionArgs } from "@remix-run/node";
import fs from 'fs'

export default function Login() {
  return (
    <div className="w-full lg:grid lg:min-h-[600px] lg:grid-cols-2 xl:min-h-[800px] h-screen">
      <div className="flex items-center justify-center py-12">
        <div className="mx-auto grid w-[375px] gap-6">
          <div className="grid gap-2 text-center">
            <h1 className="lg:hidden text-5xl my-11">OpenPipelines</h1>

            <h1 className="text-4xl">Environment Gateway</h1>
            <p className="text-balance text-muted-foreground">
              Enter <p className="inline text-black">Environment Name</p> & <p className="inline text-black">Token</p>
            </p>
          </div>
          <div className="grid gap-4">
            <div className="grid gap-2">
              <Label htmlFor="envId" className="">Name</Label>
              <Input
                id="email"
                type="text"
                placeholder="env-732.18"
                required
              />
            </div>
            <div className="grid gap-2">
              <div className="flex items-center">
                <Label htmlFor="password">Token</Label>
              </div>
              <Input id="password" type="password" required placeholder="********" />
            </div>
            <Button type="submit" className="w-full">
              Login
            </Button>
          </div>
          <div className="mt-4 text-center text-sm">
            Need a new Environment?{" "}
            <Link to="#" className="underline">
              Click here
            </Link>
          </div>
        </div>
      </div>
      <div className="hidden lg:block bg-black">
        <p className="text-white flex justify-center items-center h-screen text-7xl">OpenPipelines</p>
      </div>
    </div>
  )
}

export const meta: MetaFunction = () => {
  return [
    { title: "OpenPipelines" },
    { name: "description", content: "OpenPipelines web client" },
  ];
};